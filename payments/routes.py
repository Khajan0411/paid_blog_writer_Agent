from flask import Blueprint, redirect, session, url_for
from db.database import get_db
from db.models import User
from datetime import datetime, timedelta
from utils.auth_utils import login_required

payments_bp = Blueprint("payments", __name__)
db = get_db()

@payments_bp.route("/payment-success", methods=["GET"])
@login_required
def payment_success():
    user = db.query(User).filter(User.id == session["user_id"]).first()
    if user:
        user.subscription_expiry = datetime.utcnow() + timedelta(days=29)
        db.commit()
    return redirect(url_for("dashboard"))
