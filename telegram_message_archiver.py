# Script for archiving of telegram messages. Usefull for any subsequent anaysis.
from telegram_alerts import message_storage

# Function to archive messages
def archive_messages():
    # Open a file in write mode
    with open('telegram_message_archive.txt', 'w') as file:
        # Iterate over each message in the message_storage list
        for message in message_storage:
            # Writing the message details to the file
            file.write(f"{message}\n")

# Call the archive_messages function to execute archiving
if __name__ == "__main__":
    archive_messages()
