from functools import wraps
from modules.db_handler import db
from config import ADMINS # Theek kiya: ADMINS ko config.py se import kiya

def premium_only(func):
    @wraps(func)
    async def wrapper(client, message, *args, **kwargs):
        user = await db.users.find_one({"_id": message.from_user.id})
        if user and user.get("premium"):
            return await func(client, message, *args, **kwargs)
        await message.reply("This is a premium feature. Upgrade using /premium")
    return wrapper

def admin_only(func):
    @wraps(func)
    async def wrapper(client, message, *args, **kwargs):
        # Theek kiya: ADMINS list ka upyog kiya
        if message.from_user.id in ADMINS:
            return await func(client, message, *args, **kwargs)
        await message.reply("You are not authorized to use this command.")
    return wrapper