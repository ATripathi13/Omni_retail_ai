import random
from faker import Faker
from app.database import init_dbs, get_session
from app.models.shop_core import Product, Customer, Order, OrderItem
from app.models.ship_stream import Shipment, TrackingUpdate
from app.models.pay_guard import Wallet, Transaction
from app.models.care_desk import Ticket, Interaction
from datetime import datetime, timedelta

fake = Faker()

def seed():
    print("Initializing databases...")
    init_dbs()
    
    shop_session = get_session('shop_core')
    ship_session = get_session('ship_stream')
    pay_session = get_session('pay_guard')
    care_session = get_session('care_desk')
    
    print("Seeding Products...")
    products = []
    for _ in range(20):
        p = Product(
            name=f"{fake.word().capitalize()} {fake.word().capitalize()}",
            description=fake.paragraph(),
            price=round(random.uniform(10.0, 500.0), 2),
            stock_level=random.randint(0, 100),
            category=fake.word()
        )
        products.append(p)
    shop_session.add_all(products)
    shop_session.commit()
    
    # Reload products to get IDs
    products = shop_session.query(Product).all()
    
    print("Seeding Customers and Linked Entities...")
    for _ in range(10): # 10 Customers
        # 1. Create Customer in ShopCore
        customer = Customer(
            full_name=fake.name(),
            email=fake.email(),
            shipping_address=fake.address()
        )
        shop_session.add(customer)
        shop_session.commit() # Commit to get ID
        
        # 2. Create Wallet in PayGuard (linked by customer_id)
        wallet = Wallet(
            customer_id=customer.id,
            balance=round(random.uniform(500.0, 5000.0), 2)
        )
        pay_session.add(wallet)
        pay_session.commit()
        
        # 3. Create Orders for this Customer
        for _ in range(random.randint(1, 3)):
            order = Order(
                customer_id=customer.id,
                status=random.choice(['pending', 'shipped', 'delivered', 'cancelled']),
                total_amount=0.0
            )
            shop_session.add(order)
            shop_session.commit()
            
            # Add Items
            total = 0.0
            for _ in range(random.randint(1, 4)):
                prod = random.choice(products)
                qty = random.randint(1, 3)
                item = OrderItem(
                    order_id=order.id,
                    product_id=prod.id,
                    quantity=qty,
                    unit_price=prod.price
                )
                total += qty * prod.price
                shop_session.add(item)
            
            order.total_amount = total
            shop_session.commit()
            
            # 4. Handle Shipment (if shipped/delivered)
            if order.status in ['shipped', 'delivered']:
                shipment = Shipment(
                    order_id=order.id,
                    carrier=random.choice(['FedEx', 'UPS', 'USPS']),
                    tracking_number=fake.uuid4(),
                    status='delivered' if order.status == 'delivered' else 'in_transit',
                    estimated_delivery=datetime.utcnow() + timedelta(days=random.randint(1, 5))
                )
                ship_session.add(shipment)
                ship_session.commit()
                
                # Tracking Updates
                for i in range(random.randint(1, 3)):
                    update = TrackingUpdate(
                        shipment_id=shipment.id,
                        location=fake.city(),
                        status=random.choice(['Picked up', 'In transit', 'Arrived at facility']),
                        timestamp=datetime.utcnow() - timedelta(hours=i*4)
                    )
                    ship_session.add(update)
                ship_session.commit()
            
            # 5. Handle Payment Transaction
            txn = Transaction(
                wallet_id=wallet.id,
                order_id=order.id,
                amount=order.total_amount,
                type='debit',
                status='completed',
                created_at=order.created_at
            )
            pay_session.add(txn)
            pay_session.commit()
            
            # 6. Create Support Ticket (randomly)
            if random.random() < 0.3:
                ticket = Ticket(
                    customer_id=customer.id,
                    order_id=order.id,
                    subject=fake.sentence(),
                    status=random.choice(['open', 'closed']),
                    priority=random.choice(['low', 'medium', 'high'])
                )
                care_session.add(ticket)
                care_session.commit()
                
                # Interaction
                interaction = Interaction(
                    ticket_id=ticket.id,
                    sender='customer',
                    message=fake.text()
                )
                care_session.add(interaction)
                care_session.commit()

    print("Seeding Complete!")

if __name__ == "__main__":
    seed()
