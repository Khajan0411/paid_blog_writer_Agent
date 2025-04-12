import razorpay
from config import RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET

razorpay_client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

def create_payment_order(amount):
    order_data = {
        "amount": amount * 100,  # Razorpay accepts amount in paise
        "currency": "INR",
        "payment_capture": '1'
    }
    return razorpay_client.order.create(data=order_data)


if __name__ == "__main__":
    print(create_payment_order(599))
