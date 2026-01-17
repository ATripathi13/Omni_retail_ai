from app.orchestrator.orchestrator import Orchestrator
import sys

def main():
    orchestrator = Orchestrator()
    
    # improved default query to trigger multi-agent interaction
    default_query = "Find all orders for customer 'John Doe' (or any customer you find) and check the shipment status for them."
    
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        print("No query provided. Using default complex query example.")
        query = default_query
        
    orchestrator.run(query)

if __name__ == "__main__":
    main()
