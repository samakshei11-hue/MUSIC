from pyrogram import filters
from main import app  # Theek kiya: `app` ko main.py se import kiya gaya
from modules.db_handler import add_user

@app.on_message(filters.command("start"))
async def start(_, message):
    await add_user(message.from_user.id)
    await message.reply("Welcome to the Music Bot! /help for commands.")

@app.on_message(filters.command("help"))
async def help_cmd(_, message):
    help_text = """
    /play <song> - Play a song
    /queue - Show queue
    /pause - Pause song
    /resume - Resume song
    /stop - Stop playback
    """
    await message.reply(help_text)