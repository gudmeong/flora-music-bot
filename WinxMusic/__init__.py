import config
from WinxMusic.core.bot import WinxBot
from WinxMusic.core.dir import dirr
from WinxMusic.core.git import git
from WinxMusic.core.userbot import Userbot
from WinxMusic.misc import dbb, heroku, sudo

from .logging import LOGGER
from async_pymongo import AsyncClient
import os
# Pyrogram Client

app = WinxBot(
    name=config.BOT_USERNAME,
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    sleep_threshold=240,
    max_concurrent_transmissions=20,
    workers=min(32, (os.cpu_count() or 0) + 20),
    mongodb=dict(connection=AsyncClient(config.MONGO_DB_URI), remove_peers=True)
)

userbot = Userbot()

# Directories
dirr()

# Check Git Updates
# git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

from .platforms import PlaTForms

Platform = PlaTForms()
HELPABLE = {}
