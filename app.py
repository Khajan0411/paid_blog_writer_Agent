from flask import Flask, render_template, request, redirect, url_for, session
from db.database import get_db
from db.models import User
from utils.auth_utils import login_required
from datetime import datetime
from payments.razorpay_utils import create_payment_order

app = Flask(__name__)
app.secret_key = "secret"  # You should change this to a secure secret key
db = get_db()

# Route for the homepage
@app.route("/")
def home():
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("auth.login"))

# Route for the sign-up page
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        interest = request.form.get("interest", "")  # Optional interest field
        
        # Save to DB
        new_user = User(name=name, email=email, password=password, interest=interest)
        db.add(new_user)
        db.commit()

        session["user_id"] = new_user.id
        return redirect(url_for("dashboard"))
    return render_template("signup.html")

# Route for the login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Check if the user exists and passwords match
        user = db.query(User).filter(User.email == email, User.password == password).first()
        if user:
            session["user_id"] = user.id
            return redirect(url_for("dashboard"))
        else:
            return "Invalid login credentials", 401
    return render_template("login.html")

# Route for the payment success page
@app.route("/payment-success", methods=["GET"])
@login_required
def payment_success():
    user = db.query(User).filter(User.id == session["user_id"]).first()
    if user:
        # Set subscription to expire in 29 days
        user.subscription_expiry = datetime.utcnow() + timedelta(days=29)
        db.commit()
    return redirect(url_for("dashboard"))

# Route for the dashboard (paid/free check)
@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    user = db.query(User).filter(User.id == session["user_id"]).first()

    # Check if the user has an active subscription
    is_paid = user.subscription_expiry and user.subscription_expiry > datetime.utcnow()

    if not is_paid:
        return render_template("free_user_dashboard.html", user=user)

    return render_template("paid_user_dashboard.html", user=user)

# Route for the payment page
@app.route("/pay", methods=["GET", "POST"])
@login_required
def pay():
    # Create a payment order when user chooses to pay
    user = db.query(User).filter(User.id == session["user_id"]).first()

    if request.method == "POST":
        # Assuming Razorpay integration
        order = create_payment_order(599)  # Amount set to ₹599 for monthly subscription
        return redirect(order["short_url"])  # Redirecting to Razorpay for payment
    
    return render_template("pay.html", user=user)

# Route for logout
@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
