import abstra.workflows as aw
import os
import requests


API_TOKEN = os.getenv("SLACK_BOT_TOKEN")

slack_channels = {
    "N1": os.getenv("SLACK_CHANNEL_SUPPORT"),
    "N2": os.getenv("SLACK_CHANNEL_CS"),
    "N3": os.getenv("SLACK_CHANNEL_DEV")
}


def send_message(msg: str, channel):

    url = "https://slack.com/api/chat.postMessage"
    data = { "channel": channel, "text": msg }
    headers = { "Authorization": "Bearer " + API_TOKEN, "Content-type": "application/json; charset=utf-8" }
    
    requests.post(url, json=data, headers=headers)


level = aw.get_data("level")
conversation_info = aw.get_data("conversation")

level = "N1"
conversation_info = {
    "priority": "High",
    "message": "I need help with my account"
}

message = f"""
A new support ticket has been created with the following information:

- Priority: {conversation_info['priority']}
- Level: {level}
- Message: {conversation_info['message']}
"""

send_message(message, slack_channels[level])
