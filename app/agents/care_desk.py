from app.agents.base_agent import BaseAgent
from app.database import get_engine

class CareDeskAgent(BaseAgent):
    def __init__(self):
        engine = get_engine('care_desk')
        schema = """
Tables:
1. tickets
   - id (Integer, PK)
   - customer_id (Integer)
   - order_id (Integer, Optional)
   - subject (String)
   - status (String: 'open', 'in_progress', 'closed')
   - priority (String: 'low', 'medium', 'high')
   - created_at (DateTime)

2. interactions
   - id (Integer, PK)
   - ticket_id (Integer, FK -> tickets.id)
   - sender (String)
   - message (Text)
   - timestamp (DateTime)
        """
        super().__init__("CareDesk", engine, schema)
