from pyrogram import Client, filters
from pyrogram.types import Message
import os

# Replace these with your actual API credentials and bot token
api_id = 26074242
api_hash = 'e68320b3f73cbc927b97be3cf9192fdd'
bot_token = '7292971391:AAE6NZDS8jaAodLAU-F__LhkmwMqY-gAqsw'

# Initialize the bot client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


# # Dictionary to store chat IDs after /start command
# chat_ids = {}


# # Command handler for /start command
# @app.on_message(filters.command("start"))
# def start_command_handler(client: Client, message: Message):
#     # Get user ID of the person who sent the /start command
#     chat_id = message.from_user.id
#     chat_ids[chat_id] = None  # Initialize chat ID in dictionary
#     message.reply_text("Hello! Please send me the file name.")


# # Message handler for receiving the file name
# @app.on_message(filters.text)# & ~filters.command)
# def text_message_handler(client: Client, message: Message):
#     chat_id = message.from_user.id
    
#     if chat_id in chat_ids and chat_ids[chat_id] is None:
#         file_name = message.text.strip()

#         try:
#             with app:
#                 # Send document to the same chat where /start was initiated
#                 app.send_document(chat_id=chat_id, document=file_name, caption=f"Here is the {file_name} file.")
#                 message.reply_text(f"File '{file_name}' sent successfully!")
#         except Exception as e:
#             message.reply_text(f"Error sending file: {e}")
        
#         # Clear chat ID after sending the file
#         chat_ids.pop(chat_id, None)


# # Run the bot
# if __name__ == "__main__":
#     app.run()


# # Command handler for /start command
# @app.on_message(filters.command("start"))
# def start_command_handler(client: Client, message: Message):
#     user_id = message.from_user.id
#     message.reply_text("Hello! Here are the files available to send:\n"
#                        "/list - List all files")


# # Command handler for /list command
# @app.on_message(filters.command("list"))
# def list_files(client: Client, message: Message):
#     files = get_files_list()  # Get the list of files
#     if files:
#         file_list = "\n".join([f"{i+1}. {file}" for i, file in enumerate(files)])
#         message.reply_text(f"Available files:\n{file_list}\n\nSend /send <file_number> to send a file.")
#     else:
#         message.reply_text("No files found in the directory.")


# # Command handler for /send command with file number parameter
# @app.on_message(filters.command("send") & filters.regex(r'^\d+$'))
# def send_file_by_number(client: Client, message: Message):
#     file_number = int(message.text.split()[1]) - 1  # Extract the file number (convert to zero-index)
#     files = get_files_list()  # Get the list of files

#     if file_number < len(files):
#         file_path = files[file_number]
#         send_file(client, message, file_path)
#     else:
#         message.reply_text("Invalid file number. Send /list to see available files.")


# # Function to get a list of files in a directory
# def get_files_list():
#     directory_path = "path/to/your/directory"  # Replace with your directory path
#     if os.path.isdir(directory_path):
#         files = [file for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]
#         return files
#     else:
#         return []


# # Function to send a file
# def send_file(client: Client, message: Message, file_path: str):
#     try:
#         # Send the document back to the user who initiated the command
#         client.send_document(chat_id=message.from_user.id, document=file_path)
#         message.reply_text(f"File '{file_path}' sent successfully!")
#     except Exception as e:
#         message.reply_text(f"Error sending file: {e}")


# # Run the bot
# if __name__ == "__main__":
#     app.run()
import os
from pathlib import Path
# from pyrogram import Client, filters
# from pyrogram.types import Message

# # Replace these with your actual API credentials and bot token
# api_id = your_api_id
# api_hash = 'your_api_hash'
# bot_token = 'your_bot_token'

# Get the current directory where the script is located
current_directory = Path(__file__).parent.absolute()

# # Initialize the bot client
# app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


# Command handler for /start command
@app.on_message(filters.command("start"))
def start_command_handler(client: Client, message: Message):
    user_id = message.from_user.id
    message.reply_text("Hello! Here are the files available to send:\n"
                       "/list - List all files")


# Command handler for /list command
@app.on_message(filters.command("list"))
def list_files(client: Client, message: Message):
    files = get_files_list()  # Get the list of files
    if files:
        file_list = "\n".join([f"{i+1}. {file}" for i, file in enumerate(files)])
        message.reply_text(f"Directory: {current_directory}\n\nAvailable files:\n{file_list}\n\nSend /send <file_number> to send a file.")
    else:
        message.reply_text(f"No files found in directory: {current_directory}")


# Command handler for /send command with file number parameter
@app.on_message(filters.command("send"))# & filters.regex(r'^\d+$'))
def send_file_by_number(client: Client, message: Message):
    print("in send")
    file_number = int(message.text.split()[1]) - 1  # Extract the file number (convert to zero-index)
    files = get_files_list()  # Get the list of files

    if file_number < len(files):
        file_path = files[file_number]
        print(file_path)
        send_file(client, message, file_path)
    else:
        message.reply_text("Invalid file number. Send /list to see available files.")


# Function to get a list of files in the current directory
def get_files_list():
    if os.path.isdir(current_directory):
        files = [file.name for file in current_directory.iterdir() if file.is_file()]
        return files
    else:
        return []


# Function to send a file
def send_file(client: Client, message: Message, file_path: str):
    try:
        # Send the document back to the user who initiated the command
        client.send_document(chat_id=message.from_user.id, document=os.path.join(current_directory, file_path))
        message.reply_text(f"File '{file_path}' sent successfully!")
    except Exception as e:
        message.reply_text(f"Error sending file: {e}")


# Run the bot
if __name__ == "__main__":
    app.run()
