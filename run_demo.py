import sys
import os
import json
from app.orchestrator.orchestrator import Orchestrator
from app.core.logger import log

# Redirect logger to stdout only to avoid cluttering file logger if needed, 
# but for this script we want clean output to our log file.
# We will manually write to the demonstration log.

DEMO_LOG_FILE = "demonstration_log.txt"

QUERIES = [
    {
        "id": 1,
        "text": "Show me details for product 'Laptop X' and checking if existing stock is enough for 5 units.",
        "intent": "Product Lookup & Stock Check (ShopCore)"
    },
    {
        "id": 2,
        "text": "Find my last order and check its shipment status.",
        "intent": "Order & Shipment Status (ShopCore + ShipStream)"
    },
    {
        "id": 3,
        "text": "I have a problem with my wallet balance. Are there any open tickets?",
        "intent": "Wallet & Support Ticket Check (PayGuard + CareDesk)"
    }
]

def run_demo():
    if not os.getenv("GOOGLE_API_KEY"):
        print("ERROR: GOOGLE_API_KEY is missing. Please set it in .env")
        return

    orchestrator = Orchestrator()
    
    with open(DEMO_LOG_FILE, "w", encoding="utf-8") as f:
        f.write("=== OMNI-RETAIL AI: SUPER AGENT DEMONSTRATION LOG ===\n")
        f.write("This log fulfills Deliverable #3: A log of 3 distinct customer queries showing the 'thought process'.\n\n")
        
        for q in QUERIES:
            print(f"Running Query {q['id']}...")
            
            f.write(f"{'='*60}\n")
            f.write(f"QUERY #{q['id']}: {q['text']}\n")
            f.write(f"INTENT: {q['intent']}\n")
            f.write(f"{'='*60}\n\n")
            
            # 1. Planning Phase
            f.write("--- [PHASE 1: PLANNING] ---\n")
            f.write("Super Agent (Orchestrator) reasoning:\n")
            plan = orchestrator.plan_task(q['text'])
            
            if not plan:
                f.write("ERROR: Failed to generate plan.\n\n")
                continue
                
            f.write(json.dumps(plan, indent=2))
            f.write("\n\n")
            
            # 2. Execution Phase
            f.write("--- [PHASE 2: EXECUTION] ---\n")
            results = orchestrator.execute_plan(plan)
            
            for step in results:
                f.write(f"Step {step['step']} [{step['agent']}]:\n")
                f.write(f"  Result: {json.dumps(step['result'], default=str)}\n")
            f.write("\n")
            
            # 3. Final Answer
            f.write("--- [PHASE 3: FINAL ANSWER] ---\n")
            summary = orchestrator.summarize_results(q['text'], results)
            f.write(f"AI Response: {summary}\n\n")
            
            f.write("\n" + "#"*60 + "\n\n")

    print(f"Demonstration complete. Log written to {DEMO_LOG_FILE}")

if __name__ == "__main__":
    run_demo()
