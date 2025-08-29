from pyrogram import Client, filters
from pytgcalls import PyTgCalls  # Windows compatible 0.0.24
from pytgcalls import idle       # optional, keeps calls alive
from config import API_ID, API_HASH, BOT_TOKEN

# -------------------------------
# Pyrogram Client
# -------------------------------
app = Client(
    "MusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# -------------------------------
# PyTgCalls Initialization
# -------------------------------
pytgcalls = PyTgCalls(app)

# -------------------------------
# Handlers
# -------------------------------
import modules.user_handler
from modules.music_handler import MusicHandler
import modules.admin_handler
import modules.premium_handler
import modules.games_handler

# MusicHandler Instance
music_handler = MusicHandler(pytgcalls)

# -------------------------------
# Start Command
# -------------------------------
@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text("🎵 Music Bot is online and ready to play music!")

# -------------------------------
# Run the Bot
# -------------------------------
app.run()
