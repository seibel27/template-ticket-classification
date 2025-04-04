from abstra.tasks import get_trigger_task, send_task
from abstra.ai import prompt

task = get_trigger_task()
payload = task.get_payload()
conversation_info = payload["conversation_info"]
message = conversation_info["message"]

ans = prompt(f"""
You are a member of the support team in a software development company. You are tasked with categorizing customer support requests into three levels of support: N1, N2, and N3. Here's what each level means:

N1 (Level 1 Support):
Basic or front-line support. Requests that belong to N1 usually involve common, routine issues or questions that can be resolved quickly with general information, instructions, or simple troubleshooting steps. These requests may include:
- Password resets
- Navigation issues within the application
- Basic troubleshooting for common errors (e.g., "How do I reset my password?", "Why can't I log in?")

N2 (Level 2 Support):
More complex issues that require deeper technical knowledge or escalation to a specialized team. Requests in N2 may involve troubleshooting that requires understanding of the application's inner workings, as well as interactions between systems. Examples of N2 issues might include:
- Configuration or setup errors that require investigation
- Issues with software functionality that cannot be resolved by basic steps
- Problems with integrating external tools or services (e.g., "My system is not syncing data with the external API.")

N3 (Level 3 Support):
The highest level of support. N3 issues are often related to bugs in the system, major failures, or complex system behavior that requires development-level intervention. This level often involves escalations to software engineers or specialized support teams. N3 issues may include:
- Critical system failures or crashes
- Performance-related issues at the application or server level
- Bugs or defects that require code changes or deep system analysis (e.g., "The application crashes when performing a specific action," "There is a security vulnerability in the payment processing module.")

Based on the descriptions provided, classify the customer support request into N1, N2, or N3.

What level of support does the following request fall under?
{message}
""",
format={
    "level": {"type": "string", "enum": ["N1", "N2", "N3"]}
})

payload["level"] = ans['level'].capitalize()

send_task("triaged_conversation", payload)

task.complete()
