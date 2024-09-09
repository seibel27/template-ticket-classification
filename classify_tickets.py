import abstra.workflows as aw
from abstra.ai import prompt

message = aw.get_data("conversation")["message"]

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

aw.set_data('area', ans['area'].capitalize())
aw.set_data('priority', ans['priority'].capitalize())
