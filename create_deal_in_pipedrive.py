from abstra.tasks import get_trigger_task
from pipedrive import *

task = get_trigger_task()
payload = task.get_payload()
conversation_info = payload["conversation_info"]

existent_person = Person.retrieve_by(email=conversation_info["customer_email"])

# Create Person
if len(existent_person) == 0:
    person = Person.create(
        name=conversation_info["customer_name"],
        email=conversation_info["customer_email"]
    )

else:
    person = existent_person[0]

person_id = person.id

# Create Deal
deal = Deal.create(
    title="Deal with " + conversation_info["customer_name"],
    person_id=person_id,
    pipeline_id=Deal.Pipeline.sales,
    stage_id=Deal.Stage.sales_mapped,
)

task.complete()