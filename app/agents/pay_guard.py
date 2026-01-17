from app.agents.base_agent import BaseAgent
from app.database import get_engine

class PayGuardAgent(BaseAgent):
    def __init__(self):
        engine = get_engine('pay_guard')
        schema = """
Tables:
1. wallets
   - id (Integer, PK)
   - customer_id (Integer, Unique)
   - balance (Float)
   - currency (String)

2. transactions
   - id (Integer, PK)
   - wallet_id (Integer, FK -> wallets.id)
   - order_id (Integer)
   - amount (Float)
   - type (String: 'debit', 'credit', 'refund')
   - status (String: 'pending', 'completed', 'failed')
   - created_at (DateTime)
        """
        super().__init__("PayGuard", engine, schema)
