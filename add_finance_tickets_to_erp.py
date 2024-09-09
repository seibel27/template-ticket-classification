import abstra.workflows as aw
import abstra.tables as at

conversation_info = aw.get_data("conversation")
priority = aw.get_data("priority")

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