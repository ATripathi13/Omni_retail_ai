from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import PayBase

class Wallet(PayBase):
    __tablename__ = 'wallets'
    
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, unique=True, index=True) # Logical link to ShopCore
    balance = Column(Float, default=0.0)
    currency = Column(String, default="USD")

class Transaction(PayBase):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True, index=True)
    wallet_id = Column(Integer, ForeignKey('wallets.id'))
    order_id = Column(Integer, index=True) # Logical link to ShopCore
    amount = Column(Float)
    type = Column(String) # debit, credit, refund
    status = Column(String) # pending, completed, failed
    created_at = Column(DateTime, default=datetime.utcnow)
