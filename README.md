# Ticket Classification

## How It Works

This project automates the classification of customer tickets into different areas and levels of support and determines ticket priority using AI. The system integrates with Intercom to receive customer inputs, classifies them based on area, and routes them accordingly. It determines if a ticket falls under support, sales, or finance, and takes actions like creating deals in Pipedrive, adding records to an ERP system, sending messages via Slack and generating tickets in Intercom.

- Intercom
- Pipedrive
- Slack

To customize this template for your team and build a lot more, <a href="https://meet.abstra.app/demo?url=template-ticket-classification" target="_blank">book a demonstration here</a>.

![image](https://github.com/user-attachments/assets/431ff591-c256-4627-a169-ca30496ae5fe)


## Initial Configuration

To use this project, some initial configurations are necessary:

1. **Python Version**: Ensure Python version 3.9 or higher is installed on your system.

2. **Integrations**: This template uses the Pipedrive, Intercom, and Slack APIs. You need to have API keys to these services.
   
3. **Environment Variables**: The following environment variables are required for both local development and online deployment:

   - `INTERCOM_API_KEY`: API key for Intercom;
   - `PIPEDRIVE_API_KEY`: API key for Pipedrive;
   - `SLACK_BOT_TOKEN`: Token for Slack bot;
   - `SLACK_CHANNEL_SUPPORT`: Slack channel ID for support;
   - `SLACK_CHANNEL_CS`: Slack channel ID for customer success;
   - `SLACK_CHANNEL_DEV`: Slack channel ID for development.

   For local development, create a `.env` file at the root of the project and add the variables listed above (refer to `.env.examples`). For online deployment, configure these variables in your <a href="https://docs.abstra.io/cloud/envvars" target="_blank">environment settings</a>.

4. **Dependencies**: To install the necessary dependencies for this project, a `requirements.txt` file is provided. This file includes all the required libraries.

   Follow these steps to install the dependencies:

   1. Open your terminal and navigate to the project directory.
   2. Run the following command to install the dependencies from `requirements.txt`:

      ```sh
      pip install -r requirements.txt
      ```

5. **Local Usage**: To access the local editor with the project, use the following command:

   ```sh
      abstra editor path/to/your/project/folder/
   ```

## General Workflows

The following workflows automate the process of classifying customer tickets based on area and support level.

### New Message in Intercom

The system receives messages from Intercom through a webhook integration with the platform.

- **intercom_new_message.py**: Hook to receive and handle incoming conversations from Intercom.

### Ticket Area and Priority

AI is used to classify tickets by determining the appropriate area and priority level.

- **classify_tickets.py**: Script to classify the area (e.g., sales, finance, support) and the ticket's priority.

### Finance ERP

For tickets related to the finance area, the system automatically adds the details to the ERP.

- **add_finance_tickets_to_erp.py**: Script to add finance-related ticket data to the ERP system.

### Pipedrive Deals

For sales-related tickets, a deal is automatically created in Pipedrive.

- **create_deal_pipedrive.py**: Script to create a deal in Pipedrive for sales-related tickets.

### Classify Support Level

The system determines the appropriate support level (N1, N2, or N3) using AI.

- **classify_support_level.py**: Script to decide between N1, N2, or N3 support levels.

### Generate Intercom Ticket

The conversation is converted into an open ticket within Intercom.

- **convert_conversation_to_ticket.py**: Script to create a formal ticket in Intercom based on the conversation.

### Send Slack Message

A message containing the problem description is sent to the appropriate Slack channel, depending on the support level.

- **send_conversation_to_slack.py**: Script to send a Slack message to the corresponding channel based on the ticket's support level.

If you're interested in customizing this template for your team in under 30 minutes, <a href="https://meet.abstra.app/demo?url=template-ticket-classification" target="_blank">book a customization session here</a>.
