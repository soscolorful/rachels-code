import requests
import json

WEBHOOK_URL = "	https://webhook.site/23f16997-2d10-44b0-8414-ce928284652a"


def rachels_function():
    """
    Replace this with whatever logic you want.
    The return value will be sent to the webhook.
    """
    result = {"status": "success", "message": "Hello from Python!", "value": 42}
    return result


def send_to_rachel(data):
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        WEBHOOK_URL, headers=headers, data=json.dumps(data), timeout=10
    )
    response.raise_for_status()
    return response.status_code


if __name__ == "__main__":
    output = rachels_function()
    status_code = send_to_rachel(output)
    print(f"YEY! Rachel got your message! 😍 status code: {status_code}")
