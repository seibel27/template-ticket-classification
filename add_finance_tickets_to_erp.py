from abstra.tasks import get_trigger_task
import abstra.tables as at

task = get_trigger_task()
payload = task.get_payload()
conversation_info = payload["conversation_info"]
priority = payload["priority"]

at.insert(
    "erp",
    {
        "conversation_id": conversation_info["conversation_id"],
        "user_email": conversation_info["customer_email"],
        "user_name": conversation_info["customer_name"],
        "user_message": conversation_info["message"],
        "priority": priority
    }
) 
task.complete()