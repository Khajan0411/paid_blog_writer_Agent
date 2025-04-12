from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    interest = Column(String, nullable=True)
    password = Column(String, nullable=False)
    
    blog_url = Column(String, nullable=True)
    blog_username = Column(String, nullable=True)
    blog_password = Column(String, nullable=True)

    subscription_expiry = Column(DateTime, nullable=True)  # 👈 New column
