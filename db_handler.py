from motor.motor_asyncio import AsyncIOMotorClient
from config import URI, ADMINS

class DB:
    def __init__(self):
        self.client = AsyncIOMotorClient(URI)
        self.db = self.client["musicbot"]
        self.users = self.db.users
        self.queues = self.db.queues
        self.banned = self.db.banned

    async def add_user(self, user_id: int):
        if not await self.users.find_one({"_id": user_id}):
            await self.users.insert_one({"_id": user_id, "premium": False, "playlists": [], "banned": False})

    async def set_premium(self, user_id: int, status: bool):
        await self.users.update_one({"_id": user_id}, {"$set": {"premium": status}})

    async def add_to_queue(self, chat_id: int, song: dict):
        await self.queues.update_one({"_id": chat_id}, {"$push": {"songs": song}}, upsert=True)

    async def get_queue(self, chat_id: int):
        queue = await self.queues.find_one({"_id": chat_id})
        return queue.get("songs", []) if queue else []

    async def ban_user(self, user_id: int):
        await self.users.update_one({"_id": user_id}, {"$set": {"banned": True}})

    async def unban_user(self, user_id: int):
        await self.users.update_one({"_id": user_id}, {"$set": {"banned": False}})

db = DB()