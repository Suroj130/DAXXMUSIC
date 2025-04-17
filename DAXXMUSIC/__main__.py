import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from DAXXMUSIC import LOGGER, app, userbot, DAXX
from DAXXMUSIC.misc import sudo
from DAXXMUSIC.plugins import ALL_MODULES
from DAXXMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("No valid STRING session found. Exiting.")
        exit()

    await sudo()

    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)

        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception as e:
        LOGGER(__name__).warning(f"Error fetching banned users: {e}")

    await app.start()

    for all_module in ALL_MODULES:
        importlib.import_module("DAXXMUSIC.plugins." + all_module)
    LOGGER("DAXXMUSIC.plugins").info("All modules loaded successfully.")

    await userbot.start()
    await DAXX.start()
    await idle()

if __name__ == "__main__":
    asyncio.run(init())