import requests

def test_frontend():
    base_url = "http://127.0.0.1:8000"
    
    # 1. Check Root (Index.html)
    try:
        resp = requests.get(base_url)
        print(f"Root Check: {resp.status_code}")
        if "Omni-Retail AI" in resp.text:
            print("Title found in HTML.")
        else:
            print("Title NOT found.")
    except Exception as e:
        print(f"Root Failed: {e}")

    # 2. Check Static CSS
    try:
        resp = requests.get(f"{base_url}/static/style.css")
        print(f"CSS Check: {resp.status_code}")
        if "bg-dark" in resp.text:
            print("CSS Content found.")
    except Exception as e:
        print(f"CSS Failed: {e}")

if __name__ == "__main__":
    test_frontend()
