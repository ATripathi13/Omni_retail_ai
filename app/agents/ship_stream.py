from app.agents.base_agent import BaseAgent
from app.database import get_engine

class ShipStreamAgent(BaseAgent):
    def __init__(self):
        engine = get_engine('ship_stream')
        schema = """
Tables:
1. shipments
   - id (Integer, PK)
   - order_id (Integer, Unique)
   - carrier (String)
   - tracking_number (String, Unique)
   - status (String: 'processing', 'in_transit', 'delivered')
   - estimated_delivery (DateTime)

2. tracking_updates
   - id (Integer, PK)
   - shipment_id (Integer, FK -> shipments.id)
   - location (String)
   - status (String)
   - timestamp (DateTime)
        """
        super().__init__("ShipStream", engine, schema)
