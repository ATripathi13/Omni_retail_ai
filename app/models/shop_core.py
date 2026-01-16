from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import ShopBase

class Product(ShopBase):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    price = Column(Float)
    stock_level = Column(Integer)
    category = Column(String)

class Customer(ShopBase):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True, index=True)
    shipping_address = Column(Text)
    
class Order(ShopBase):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    status = Column(String, default="pending") # pending, shipped, delivered, cancelled
    created_at = Column(DateTime, default=datetime.utcnow)
    total_amount = Column(Float, default=0.0)
    
    items = relationship("OrderItem", back_populates="order")

class OrderItem(ShopBase):
    __tablename__ = 'order_items'
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    unit_price = Column(Float)
    
    order = relationship("Order", back_populates="items")
