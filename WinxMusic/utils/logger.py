from pyrogram.types import Message

from WinxMusic import app
from WinxMusic.utils.database import is_on_off
from config import LOG, LOG_GROUP_ID


async def play_logs(message: Message, streamtype: str):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "🔒 Private Group"

        logger_text = f"""
🎵 **Reproduction Record - {app.mention}** 🎵

📌 **Chat ID:** `{message.chat.id}`
🏷️ **Chat Name:** {message.chat.title}
🔗 **Chat Username:** {chatusername}

👤 **UserID:** `{message.from_user.id}`
📛 **Name:** {message.from_user.mention}
📱 **Username:** @{message.from_user.username}

🔍 **Keyword:** {message.text.split(None, 1)[1]}
🎧 **Transmission Type:** {streamtype}"""

        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    chat_id=LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except Exception:
                pass
        return
