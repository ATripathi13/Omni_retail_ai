import google.generativeai as genai
import os
import json
import re
from app.agents.shop_core import ShopCoreAgent
from app.agents.ship_stream import ShipStreamAgent
from app.agents.pay_guard import PayGuardAgent
from app.agents.care_desk import CareDeskAgent
from dotenv import load_dotenv
from app.core.logger import log

load_dotenv()

class Orchestrator:
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
             log.warning("GOOGLE_API_KEY not found.")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
        
        # Initialize Sub-Agents
        self.agents = {
            "ShopCore": ShopCoreAgent(),
            "ShipStream": ShipStreamAgent(),
            "PayGuard": PayGuardAgent(),
            "CareDesk": CareDeskAgent()
        }

    def plan_task(self, user_query):
        """
        Decomposes the user query into a list of executable steps.
        """
        prompt = f"""
You are the Orchestrator for an Omni-Retail AI system.
You have access to 4 specialized agents:
1. ShopCore: Products, Customers, Orders, Order Items.
2. ShipStream: Shipments, Tracking Updates.
3. PayGuard: Wallets, Transactions.
4. CareDesk: Support Tickets, Interactions.

Goal: Decompose the User Query into a sequential JSON plan.
Format:
[
  {{
    "id": 1,
    "agent": "AgentName",
    "goal": "Description of what to find",
    "query": "Natural language query for the agent"
  }},
  ...
]

Rules:
- If info from Step 1 is needed for Step 2, mention it in the query (e.g., "Use the Order ID from step 1...").
- Return ONLY the raw JSON array.

User Query: "{user_query}"
        """
        try:
            response = self.model.generate_content(prompt)
            plan_text = response.text.strip()
            # Clean markdown
            plan_text = re.sub(r"```json\s*", "", plan_text)
            plan_text = re.sub(r"```\s*$", "", plan_text)
            return json.loads(plan_text)
        except Exception as e:
            log.error(f"Planning Error: {e}")
            log.warning("FALLBACK: generating hardcoded plan for demo.")
            # Fallback plan for the default query
            return [
                {
                    "id": 1,
                    "agent": "ShopCore",
                    "goal": "Find customer ID",
                    "query": "Find customer details for 'John Doe'"
                },
                {
                    "id": 2,
                    "agent": "ShopCore",
                    "goal": "Find orders for customer",
                    "query": "Find orders for customer ID from step 1"
                },
                {
                    "id": 3,
                    "agent": "ShipStream",
                    "goal": "Check shipment status",
                    "query": "Check status for order IDs from step 2"
                }
            ]

    def execute_plan(self, plan):
        context = {}
        results = []
        
        log.info(f"--- Executing Plan ({len(plan)} steps) ---")
        for step in plan:
            step_id = step['id']
            agent_name = step['agent']
            query = step['query']
            
            log.info(f"Step {step_id} [{agent_name}]: {query}")
            
            # Enrich query with previous context if needed
            if context:
                query += f"\n\nContext from previous steps: {json.dumps(context, default=str)}"
            
            agent = self.agents.get(agent_name)
            if not agent:
                log.error(f"Error: Unknown agent {agent_name}")
                continue
                
            result = agent.process_query(query)
            
            # Store result
            context[f"step_{step_id}_result"] = result
            results.append({
                "step": step_id,
                "agent": agent_name,
                "result": result
            })
            
            # Simple print of result
            if "error" in result:
                log.error(f"  -> Error: {result['error']}")
            elif "data" in result:
                data = result["data"]
                log.info(f"  -> Found {len(data)} records.")
            else:
                log.info(f"  -> {result}")
                
        return results

    def run(self, user_query):
        log.info(f"User Query: {user_query}")
        plan = self.plan_task(user_query)
        if not plan:
            log.error("Failed to generate a plan.")
            return
        
        log.info("Generated Plan:")
        log.info(json.dumps(plan, indent=2))
        
        return self.execute_plan(plan)
