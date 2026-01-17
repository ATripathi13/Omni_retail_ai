from app.agents.base_agent import BaseAgent
from app.database import get_engine

class ShopCoreAgent(BaseAgent):
    def __init__(self):
        engine = get_engine('shop_core')
        schema = """
Tables:
1. products
   - id (Integer, PK)
   - name (String)
   - description (Text)
   - price (Float)
   - stock_level (Integer)
   - category (String)

2. customers
   - id (Integer, PK)
   - full_name (String)
   - email (String)
   - shipping_address (Text)

3. orders
   - id (Integer, PK)
   - customer_id (Integer, FK -> customers.id)
   - status (String: 'pending', 'shipped', 'delivered', 'cancelled')
   - created_at (DateTime)
   - total_amount (Float)

4. order_items
   - id (Integer, PK)
   - order_id (Integer, FK -> orders.id)
   - product_id (Integer, FK -> products.id)
   - quantity (Integer)
   - unit_price (Float)
        """
        super().__init__("ShopCore", engine, schema)
