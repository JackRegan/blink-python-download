# To run :
# source .venv/bin/activate
# python download_blink_clips.py

import asyncio
from blinkpy.blinkpy import Blink
from blinkpy.auth import Auth
from aiohttp import ClientSession
import os
import getpass

EMAIL = "paulregan73@gmail.com"
DOWNLOAD_DIR = "blink_clips"

async def run_blink_clip_download(password: str):
    async with ClientSession() as session:
        blink = Blink(session=session)
        blink.auth = Auth({"username": EMAIL, "password": password}, session=session)
        await blink.start()
        await blink.refresh()

        os.makedirs(DOWNLOAD_DIR, exist_ok=True)

        print("\n🔎 Cameras found:", list(blink.cameras.keys()))
        print("Attempting to download all available clips using blinkpy's download_videos...")
        await blink.download_videos(path=DOWNLOAD_DIR, since="1970-01-01T00:00:00+0000")

if __name__ == "__main__":
    print("Blink Clip Downloader")
    print(f"Using saved email: {EMAIL}")
    password = getpass.getpass("Blink Password: ")

    try:
        asyncio.run(run_blink_clip_download(password))
    except Exception as e:
        print(f"\n❌ Error: {e}")