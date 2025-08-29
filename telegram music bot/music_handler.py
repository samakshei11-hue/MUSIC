import asyncio
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.exceptions import NoActiveGroupCall
from utils.yt_utils import download_audio

class MusicHandler:
    def __init__(self, pytgcalls: PyTgCalls):
        self.pytgcalls = pytgcalls

    async def play_song(self, client, chat_id, song_url):
        try:
            # Bug fix: InputAudioStream ka sahi upyog kiya gaya hai
            song_path = await download_audio(song_url)
            if not song_path:
                return "Gaana download nahi kiya ja saka."

            await self.pytgcalls.join_group_call(
                chat_id,
                InputAudioStream(song_path)
            )
            return "Gaana bajna shuru ho gaya."
        except NoActiveGroupCall:
            return "Kripya pehle voice chat shuru karen."
        except Exception as e:
            return f"Error: {e}"

    async def skip_song(self, chat_id):
        # Bug fix: KeyError se bachne ke liye check joda gaya
        if chat_id not in self.pytgcalls.active_calls:
            return "Koi gaana nahi baj raha hai."
        # Logic: pop first song from DB queue and play next
        # ...

    async def pause_song(self, chat_id):
        try:
            await self.pytgcalls.pause_stream(chat_id)
            return "Gaana pause ho gaya."
        except Exception:
            return "Koi gaana nahi baj raha hai."

    async def resume_song(self, chat_id):
        try:
            await self.pytgcalls.resume_stream(chat_id)
            return "Gaana dobara shuru ho gaya."
        except Exception:
            return "Koi gaana nahi baj raha hai."

    async def stop_song(self, chat_id):
        try:
            await self.pytgcalls.leave_group_call(chat_id)
            return "Playback band ho gaya."
        except Exception:
            return "Koi gaana nahi baj raha hai."