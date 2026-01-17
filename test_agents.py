from app.agents.shop_core import ShopCoreAgent
from app.agents.ship_stream import ShipStreamAgent
from app.agents.pay_guard import PayGuardAgent
from app.agents.care_desk import CareDeskAgent
import os

def test_agents():
    print("Testing Agents...")
    if not os.getenv("GOOGLE_API_KEY"):
        print("ERROR: GOOGLE_API_KEY is missing. Please set it before running tests.")
        return

    # 1. ShopCore Test
    print("\n--- ShopCore Agent ---")
    shop_agent = ShopCoreAgent()
    res = shop_agent.process_query("Show me 3 products under $100.")
    print(res)

    # 2. ShipStream Test
    print("\n--- ShipStream Agent ---")
    ship_agent = ShipStreamAgent()
    # Assuming we have some shipments from seeding, prompt broadly
    res = ship_agent.process_query("List the status of all shipments.")
    print(res)

    # 3. PayGuard Test
    print("\n--- PayGuard Agent ---")
    pay_agent = PayGuardAgent()
    res = pay_agent.process_query("What is the average wallet balance?")
    print(res)

    # 4. CareDesk Test
    print("\n--- CareDesk Agent ---")
    care_agent = CareDeskAgent()
    res = care_agent.process_query("How many open tickets are there?")
    print(res)

import traceback

if __name__ == "__main__":
    try:
        test_agents()
    except Exception:
        with open("agent_error.log", "w") as f:
            f.write(traceback.format_exc())
        print("An error occurred. Check agent_error.log")
