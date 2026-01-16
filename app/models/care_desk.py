from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import CareBase

class Ticket(CareBase):
    __tablename__ = 'tickets'
    
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, index=True) # Logical link to ShopCore
    order_id = Column(Integer, nullable=True) # Optional link
    subject = Column(String)
    status = Column(String, default="open") # open, in_progress, closed
    priority = Column(String, default="medium")
    created_at = Column(DateTime, default=datetime.utcnow)
    
    interactions = relationship("Interaction", back_populates="ticket")

class Interaction(CareBase):
    __tablename__ = 'interactions'
    
    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey('tickets.id'))
    sender = Column(String) # 'customer' or 'agent'
    message = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    ticket = relationship("Ticket", back_populates="interactions")
