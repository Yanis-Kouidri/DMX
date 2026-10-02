import os
from dotenv import load_dotenv
from telegram import Bot

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupération des variables avec une sécurité
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Vérification de la présence des identifiants
if not TOKEN or not CHAT_ID:
    raise ValueError("Error : TELEGRAM_TOKEN or TELEGRAM_CHAT_ID missing in .env file. Please add them")


async def send_telegram_message(text):
    bot = Bot(token=TOKEN)
    
    async with bot:
        await bot.send_message(chat_id=CHAT_ID, text=text)
        #print("Telegram message successfully sent")
