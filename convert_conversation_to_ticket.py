import abstra.workflows as aw
import requests
import os


API_KEY = os.getenv("INTERCOM_API_KEY")
conversation = aw.get_data("conversation")


# post request to "https://api.intercom.io/ticket_types"
# list ticket types
ticket_type_id = '1'

url = "https://api.intercom.io/conversations/" + conversation["conversation_id"] + "/convert"

headers = {
    "Content-Type": "application/json",
    "Intercom-Version": "2.11",
    "Authorization": f"Bearer {API_KEY}"
}

payload = {
    "ticket_type_id": ticket_type_id
}

response = requests.post(url, headers=headers, json=payload)

print(response.json())