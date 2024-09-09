import abstra.hooks as ah
import abstra.workflows as aw


def name_from_email(email: str):
    return " ".join([e.capitalize() for e in email.split("@")[0].split(".")])

# Use Abstra Hooks to create Python endpoints
body, query, headers = ah.get_request()

print(body)

topic = body['topic']

if topic == 'conversation.user.created':

    info = {
        "message": body['data']['item']['source']['body'],
        "conversation_id": body['data']['item']['id'],
        "customer_email": body['data']['item']['source']['author']['email'],
        "customer_name": name_from_email(body['data']['item']['source']['author']['name']),
    }

    if info['message'].startswith('<p>'): 
        info['message'] = info['message'][3:]

    if info['message'].endswith('</p>'):
        info['message'] = info['message'][:-4]
        
    aw.set_data("conversation", info)
    aw.set_data("topic", "New_Conversation")