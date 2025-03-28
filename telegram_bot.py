# 1. Create a Telegram Bot:
#  - Open Telegram and start a conversation with the BotFather by searching for @BotFather.
#  - Send /start to initialize the conversation.
#  - Then, send /newbot to create a new bot.
#  - Follow the prompts to name your bot and set a username. BotFather will provide you with an API token.
# 2. Get Your Chat ID:
#  - Send a message to your bot from your Telegram account.
#  - Use the Telegram API to fetch updates and find your chat ID. You can do this by visiting https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates in your browser, where <YOUR_BOT_TOKEN> is replaced with your actual bot token. Look for your chat ID in the JSON response under message -> chat -> id.
# 3. Install the Necessary Library:
#  - In your Jupyter Notebook, install the python-telegram-bot library if you haven't already
#  - Run this code 
import asyncio
import nest_asyncio
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import requests
import json

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

# Telegram Bot Configuration
BOT_TOKEN = 'YOUR_BOT_TOKEN'
CHAT_ID = 'YOUR_CHAT_ID'

# API Configuration
URL = "https://api.airia.ai/v1/PipelineExecution/12345678901234567890"
API_KEY = "ak-MTc2NDU..................XXXXXXXXXXOSAg"

async def fetch_answer_from_api(query):
    payload = json.dumps({
        "userInput": query,
        "asyncOutput": False
    })
    headers = {
        "X-API-KEY": API_KEY,
        "Content-Type": "application/json"
    }
    
    response = requests.request("POST", URL, headers=headers, data=payload)
    return json.loads(response.text).get('result', 'No response from API.')

async def send_message(bot, chat_id, message):
    await bot.send_message(chat_id=chat_id, text=message)

async def handle_message(update: Update, context):
    question = update.message.text
    answer = await fetch_answer_from_api(question)
    await send_message(context.bot, update.effective_chat.id, answer)

async def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    await application.run_polling()

# Run the bot using the current event loop
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
