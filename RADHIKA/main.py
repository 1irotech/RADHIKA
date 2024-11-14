import logging
import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ChatAction
from pyrogram.types import BotCommand, Message, InlineKeyboardButton, InlineKeyboardMarkup
from pymongo import MongoClient
import random

# Set up logging for simple output
logging.basicConfig(level=logging.INFO)

# Environment variables
API_ID = os.environ.get("API_ID", "16457832")
API_HASH = os.environ.get("API_HASH", "3030874d0befdb5d05597deacc3e83ab")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7383809543:AAE1JNivQ81ZMoP7aC_FRDpRKByjahmBDTI")
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://teamdaxx123:teamdaxx123@cluster0.ysbpgcp.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = "7400383704"

# MongoDB connection
try:
    client = MongoClient(MONGO_URL, connectTimeoutMS=30000, serverSelectionTimeoutMS=30000)
    client.server_info()  # Check if connection is successful
    logging.info("MongoDB connection successful!")
except Exception as e:
    logging.error(f"MongoDB connection error: {e}")
    exit()

# Initialize MongoDB collections
db = client.get_database("Word")  # Ensure you access the correct database
chatai = db.get_collection("WordDb")  # Ensure this is the correct collection
clonebotdb = db.get_collection("CloneBotDb")  # Ensure this is the correct collection

# Initialize the main bot client
RADHIKA = Client(
    "chat-gpt",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Define the anony_boot function to start the main bot
async def anony_boot():
    try:
        # Start the bot
        await RADHIKA.start()
        logging.info(f"Bot @{RADHIKA.me.username} started successfully.")
        
        # Set bot commands
        await RADHIKA.set_bot_commands([
            BotCommand("start", "Start the bot"),
            BotCommand("help", "Get the help menu"),
            BotCommand("clone", "Clone a bot"),
            BotCommand("stats", "Get bot stats"),
            BotCommand("cloned", "List all cloned bots"),
            BotCommand("delclone", "Delete a cloned bot"),
            BotCommand("delallclone", "Delete all cloned bots"),
        ])
        logging.info("Bot commands set successfully.")
        
    except Exception as ex:
        logging.error(f"Error during bot startup: {ex}")
        return

# Command handler for /start
@RADHIKA.on_message(filters.command("start") & filters.private)
async def start(client: Client, message: Message):
    keyboard = [
        [InlineKeyboardButton("Join 🤒", url="https://t.me/BABY09_WORLD")]
    ]
    await message.reply(
        "Hii, I am Radhika Baby, How are you?",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# Command handler for /help
@RADHIKA.on_message(filters.command("help") & filters.private)
async def help(client: Client, message: Message):
    await message.reply("This is a bot that does X, Y, and Z.\nUse /start to begin!")

# Clone Bot Logic
@RADHIKA.on_message(filters.command(["clone", "host", "deploy"]))
async def clone_txt(client, message: Message):
    if len(message.command) > 1:
        bot_token = message.command[1].strip()
        mi = await message.reply_text("Please wait while I check the bot token.")
        
        try:
            # Create a unique session name for each cloned bot
            session_name = f"clone_{bot_token}"
            ai = Client(session_name, API_ID, API_HASH, bot_token=bot_token)

            # Register command handlers for the cloned bot
            @ai.on_message(filters.command("start") & filters.private)
            async def start_clone(client: Client, message: Message):
                keyboard = [
                    [InlineKeyboardButton("Join 🤒", url="https://t.me/BABY09_WORLD")]
                ]
                await message.reply(
                    "Hii, I am your cloned bot, How are you?",
                    reply_markup=InlineKeyboardMarkup(keyboard)
                )

            @ai.on_message(filters.command("help") & filters.private)
            async def help_clone(client: Client, message: Message):
                await message.reply("This is a cloned bot with the same functionality as the main bot.")

            # Start the cloned bot and keep it running
            await ai.start()  # Start the cloned bot
            
            # Get bot details
            bot = await ai.get_me()
            bot_id = bot.id
            user_id = message.from_user.id

            details = {
                "bot_id": bot.id,
                "is_bot": True,
                "user_id": user_id,
                "name": bot.first_name,
                "token": bot_token,
                "username": bot.username,
            }

            # Insert the details into MongoDB
            clonebotdb.insert_one(details)

            # Respond to the user
            await mi.edit_text(f"**Bot @{bot.username} has been successfully cloned ✅.**")
            logging.info(f"Cloned bot @{bot.username} started successfully.")

            # Keep the cloned bot running
            await ai.run()  # This will keep the bot running and respond to commands

        except Exception as e:
            logging.error(f"Error while cloning bot: {e}")
            await mi.edit_text(f"⚠️ Error: {e}")
    else:
        await message.reply_text("**Provide Bot Token after /clone Command from @Botfather.**")

# List cloned bots: /cloned command
@RADHIKA.on_message(filters.command("cloned"))
async def list_cloned_bots(client, message: Message):
    try:
        cloned_bots = await clonebotdb.find().to_list(length=None)
        if not cloned_bots:
            await message.reply_text("No bots have been cloned yet.")
            return
        total_clones = len(cloned_bots)
        text = f"**Total Cloned Bots:** {total_clones}\n\n"
        for bot in cloned_bots:
            text += f"**Bot ID:** {bot['bot_id']}\n"
            text += f"**Bot Name:** {bot['name']}\n"
            text += f"**Bot Username:** @{bot['username']}\n\n"
        await message.reply_text(text)
    except Exception as e:
        logging.exception(e)
        await message.reply_text("**An error occurred while listing cloned bots.**")

# Delete cloned bot: /delclone command
@RADHIKA.on_message(filters.command(["deletecloned", "delcloned", "delclone", "deleteclone", "removeclone", "cancelclone"]))
async def delete_cloned_bot(client, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("**⚠️ Please provide the bot token after the command.**")
            return

        bot_token = " ".join(message.command[1:])
        ok = await message.reply_text("**Checking the bot token...**")

        cloned_bot = await clonebotdb.find_one({"token": bot_token})

        if cloned_bot is None:
            await message.reply_text("**⚠️ The provided bot token is not in the cloned list.**")
            return

        # If the bot is found, delete it from the database
        await clonebotdb.delete_one({"token": bot_token})

        # Stop the cloned bot's client session (this is where we stop the cloned bot)
        await ok.edit_text(f"**🤖 your cloned bot has been disconnected from my server ☠️**")

    except Exception as e:
        await message.reply_text(f"**An error occurred while deleting the cloned bot:** {e}")
        logging.exception(e)

# Delete all cloned bots: /delallclone command
@RADHIKA.on_message(filters.command("delallclone") & filters.user(OWNER_ID))
async def delete_all_cloned_bots(client, message: Message):
    try:
        a = await message.reply_text("**Deleting all cloned bots...**")
        await clonebotdb.delete_many({})
        await a.edit_text("**All cloned bots have been deleted successfully ✅**")
    except Exception as e:
        await a.edit_text(f"**An error occurred while deleting all cloned bots.** {e}")
        logging.exception(e)

# Private and Group chats handler (both text and stickers)
@RADHIKA.on_message(filters.text | filters.sticker)
async def chat_handler(client: Client, message: Message):
    # Check if the message is from a private chat
    if message.chat.type == "private":
        await handle_chat(message)
    elif message.chat.type in ["group", "supergroup"]:
        await handle_chat(message)

async def handle_chat(message: Message):
    # Handle the chat logic for both private and group messages
    K = []  
    is_chat = chatai.find({"word": message.text})
    for x in is_chat:
        K.append(x['text'])

    if K:
        hey = random.choice(K)
        is_text = chatai.find_one({"text": hey})
        Yo = is_text['check']
        if Yo == "sticker":
            await message.reply_sticker(f"{hey}")
        else:
            await message.reply_text(f"{hey}")

# Main entry point to run the bot
if __name__ == "__main__":
    try:
        logging.info("Starting bot...")
        asyncio.get_event_loop().create_task(anony_boot())
        asyncio.get_event_loop().run_forever()
    except Exception as e:
        logging.error(f"Failed to start the bot: {e}")
        
