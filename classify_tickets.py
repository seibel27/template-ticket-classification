from abstra.tasks import get_trigger_task, send_task
from abstra.ai import prompt

task = get_trigger_task()
payload = task.get_payload()
conversation_info = payload["conversation_info"]
message = conversation_info["message"]

categories = [
    {
        "area": "Support",
        "description": "The customer is having trouble using the software or is having technical issues"
    },
    {
        "area": "Finance",
        "description": "The customer is having trouble with the payment, wants to cancel or wants to upgrade their plan"
    },
    {
        "area": "Sales",
        "description": "The customer wants to know more about the product or is interested in buying"
    }
]

ans = prompt(f"""You are a member of the support team. You have received a message from a customer. Your job is to decide in which area this message belongs to, the options are: {", ".join([f"{c['area']}: {c['description']}" for c in categories])}. Furthermore, you must decide what is the priority of this message, the options are: low, medium, high, critical. Take the following factors into consideration: Is the problem time sensitive? Is the problem affecting multiple customers? Can this problem result in future problems?
            
            Message: {message}""",
            format={
                "area": {"type": "string", "description": "The area of the message"},
                "priority": {"type": "string", "description": "The priority of the message"}
            })

payload["area"] = ans['area'].capitalize()
payload["priority"] = ans['priority'].capitalize()

# Classifying by area
areas_list = "Support,Finance,Sales".split(",")
area = ans['area'].capitalize()
for areas in areas_list:
    if area is not None and area == areas:
        send_task(area, payload)

task.complete()
