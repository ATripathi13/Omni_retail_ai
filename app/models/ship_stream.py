from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import ShipBase

class Shipment(ShipBase):
    __tablename__ = 'shipments'
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, unique=True, index=True) # Logical link to ShopCore
    carrier = Column(String)
    tracking_number = Column(String, unique=True)
    status = Column(String) # processing, in_transit, delivered
    estimated_delivery = Column(DateTime)
    
    updates = relationship("TrackingUpdate", back_populates="shipment")

class TrackingUpdate(ShipBase):
    __tablename__ = 'tracking_updates'
    
    id = Column(Integer, primary_key=True, index=True)
    shipment_id = Column(Integer, ForeignKey('shipments.id'))
    location = Column(String)
    status = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    shipment = relationship("Shipment", back_populates="updates")
