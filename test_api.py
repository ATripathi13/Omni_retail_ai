import requests
import json
import time

def test_api():
    base_url = "http://127.0.0.1:8000"
    
    # Wait for server to start
    print("Waiting for server...")
    time.sleep(3)
    
    # 1. Health Check
    try:
        resp = requests.get(f"{base_url}/health")
        print(f"Health Check: {resp.status_code}")
        print(resp.json())
    except Exception as e:
        print(f"Health Check Failed: {e}")
        return

    # 2. Chat Endpoint
    payload = {"query": "Find customer John Doe"}
    try:
        resp = requests.post(f"{base_url}/api/v1/chat", json=payload)
        print(f"\nChat Check: {resp.status_code}")
        if resp.status_code == 200:
            data = resp.json()
            print("Plan generated:", len(data.get("plan", [])))
            print("Results found:", len(data.get("results", [])))
        else:
            print(resp.text)
    except Exception as e:
        print(f"Chat Check Failed: {e}")

if __name__ == "__main__":
    test_api()
