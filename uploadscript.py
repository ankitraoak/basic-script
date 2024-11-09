from pyrogram import Client, filters
from pyrogram.types import Message
from zipfile import ZipFile
import os


# Replace these with your actual API credentials and bot token
api_id = 26074242
api_hash = 'e68320b3f73cbc927b97be3cf9192fdd'
bot_token = '7431350058:AAHsOlY9p383D3XysLE2D_SsZiu0h2ZLTvE'

# Initialize the bot client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)



from pathlib import Path
current_directory = Path(__file__).parent.absolute()


# Command handler for /start command
@app.on_message(filters.command("start"))
async def start_command_handler(client: Client, message: Message):
    await message.reply_text("Hello! Here are the files available to send:\n"
                             "/list - List all files")

    # await message.reply_text("Hello! Here are the files available to send:\n"
    #                    "/list - List all files")


# Command handler for /list command
@app.on_message(filters.command("list"))
async def list_files(client: Client, message: Message):
    files = get_files_list()  # Get the list of files
    if files:
        file_list = "\n".join([f"{i+1}. {file}" for i, file in enumerate(files)])
        await message.reply_text(f"Directory: {current_directory}\n\nAvailable files:\n{file_list}\n\nSend /send <file_number> to send a file.")
    else:
        await message.reply_text(f"No files found in directory: {current_directory}")


# Command handler for /send command with file number parameter
@app.on_message(filters.command("send"))# & filters.regex(r'^\d+$'))
async def send_file_by_number(client: Client, message: Message):
    print("in send")
    file_number = int(message.text.split()[1]) - 1  # Extract the file number (convert to zero-index)
    files = get_files_list()  # Get the list of files

    if file_number < len(files):
        file_path = files[file_number]
        print(file_path)
        await send_file(client, message, file_path)
    else:
        await message.reply_text("Invalid file number. Send /list to see available files.")


# Function to get a list of files in the current directory
def get_files_list():
    if os.path.isdir(current_directory):
        files = [file.name for file in current_directory.iterdir() if file.is_file()]
        return files
    else:
        return []


# Function to send a file
async def send_file(client: Client, message: Message, file_path: str):
    try:
        # Send the document back to the user who initiated the command
        await client.send_document(
    chat_id=-1002003609759, 
    document=os.path.join(current_directory, file_path),
    caption=os.path.basename(file_path)  # This sets the caption to the file name
)
        await message.reply_text(f"File '{file_path}' sent successfully!")
    except Exception as e:
        await message.reply_text(f"Error sending file: {e}")

@app.on_message(filters.command("zip"))
async def zip_directory(client: Client, message: Message):
    try:
        zip_filename = "uploader11.zip"  # Name of the zip file
        zip_path = os.path.join(current_directory, zip_filename)

        # Create the zip file
        with ZipFile(zip_path, 'w') as zipf:
            for foldername, subfolders, filenames in os.walk(current_directory):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)
                    zipf.write(file_path, os.path.relpath(file_path, current_directory))

        await message.reply_document(zip_path)  # Send the zip file to the user
    except Exception as e:
        print(e)

# Run the bot
if __name__ == "__main__":
    app.run()
