import os
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
SECRET_KEY = os.getenv("SECRET_KEY")
RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET")
DATABASE_URL = os.getenv("DATABASE_URL")
BLOG_AGENT_API_KEY = os.getenv("BLOG_AGENT_API_KEY")
PAID_PLAN_AMOUNT = int(os.getenv("PAID_PLAN_AMOUNT", 599))
PLAN_DURATION_DAYS = int(os.getenv("PLAN_DURATION_DAYS", 29))
