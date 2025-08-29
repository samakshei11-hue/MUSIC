from pyrogram import filters
from main import app  # Theek kiya: `app` ko main.py se import kiya gaya
from modules.decorators import premium_only

@app.on_message(filters.command("highqualityplay"))
@premium_only
async def high_quality_play(_, message):
    await message.reply("Playing in CD quality!")