import requests

WEBHOOK_URL = "https://webhook.site/215f08cb-d2f9-4d71-abb1-be974d0fca01"

if __name__ == "__main__":
    r = requests.post(
        WEBHOOK_URL, json={"type": "output", "line": "hello world"}, timeout=10
    )
    print("Webhook status:", r.status_code)
