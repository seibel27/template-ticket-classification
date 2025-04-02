from abstra.tasks import get_trigger_task, send_task
import requests
import os

task = get_trigger_task()
payload = task.get_payload()
conversation_info = payload["conversation_info"]

API_KEY = os.getenv("INTERCOM_API_KEY")


# post request to "https://api.intercom.io/ticket_types"
# list ticket types
ticket_type_id = '1'

url = "https://api.intercom.io/conversations/" + conversation_info["conversation_id"] + "/convert"

headers = {
    "Content-Type": "application/json",
    "Intercom-Version": "2.11",
    "Authorization": f"Bearer {API_KEY}"
}

payload_json = {
    "ticket_type_id": ticket_type_id
}

response = requests.post(url, headers=headers, json=payload_json)

print(response.json())