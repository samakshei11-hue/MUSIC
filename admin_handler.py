from pyrogram import filters
from main import app  # Theek kiya: app ko main.py se import kiya
from modules.db_handler import db

# Theek kiya: admin_only decorator joda gaya
def admin_only(func):
    async def wrapper(_, message):
        if not await db.is_admin(message.from_user.id):
            await message.reply_text("Aapke paas is command ka upyog karne ki anumati nahi hai.")
            return
        await func(_, message)
    return wrapper

@app.on_message(filters.command("ban"))
@admin_only
async def ban(_, message):
    if len(message.command) < 2:
        await message.reply_text("Kripya user ID de. Udaharan: /ban 123456789")
        return
    try:
        user_id = int(message.command[1])
        await db.ban_user(user_id)
        await message.reply_text(f"User {user_id} banned!")
    except (ValueError, IndexError):
        await message.reply_text("Invalid user ID.")

@app.on_message(filters.command("unban"))
@admin_only
async def unban(_, message):
    if len(message.command) < 2:
        await message.reply_text("Kripya user ID de. Udaharan: /unban 123456789")
        return
    try:
        user_id = int(message.command[1])
        await db.unban_user(user_id)
        await message.reply_text(f"User {user_id} unbanned!")
    except (ValueError, IndexError):
        await message.reply_text("Invalid user ID.")