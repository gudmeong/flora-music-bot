from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from WinxMusic import app
from WinxMusic.utils.database import (
    delete_served_chat,
    get_assistant,
    is_on_off,
)
from config import LOG, LOG_GROUP_ID


@app.on_message(filters.new_chat_members)
async def on_bot_added(_, message: Message):
    try:
        if not await is_on_off(LOG):
            return
        userbot = await get_assistant(message.chat.id)
        chat = message.chat
        for members in message.new_chat_members:
            if members.id == app.id:
                count = await app.get_chat_members_count(chat.id)
                username = (
                    message.chat.username if message.chat.username else "ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
                )
                msg = (
                f"🎉 Music bot added in a new group #added \n\n"
                f"📋 Chat Name: {message.chat.title}\n"
                f"🆔 Chat ID: { message.chat.id }\n"
                f"🔗 Chat Username: @{username}\n"
                f"👥 Number of Chat Members: {count}\n"
                f"👤 Added by: {message.from_user.mention}"
                )
                await app.send_message(
                    LOG_GROUP_ID,
                    text=msg,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text=f"Added by: {message.from_user.first_name}",
                                    user_id=message.from_user.id,
                                )
                            ]
                        ]
                    ),
                )
                if message.chat.username:
                    await userbot.join_chat(message.chat.username)
    except Exception:
        pass


@app.on_message(filters.left_chat_member)
async def on_bot_kicked(_, message: Message):
    try:
        if not await is_on_off(LOG):
            return
        userbot = await get_assistant(message.chat.id)

        left_chat_member = message.left_chat_member
        if left_chat_member and left_chat_member.id == app.id:
            remove_by = (
                message.from_user.mention
                if message.from_user
                else "Usuário Desconhecido"
            )
            title = message.chat.title
            username = (
                f"@{message.chat.username}" if message.chat.username else "Chat Privado"
            )
            chat_id = message.chat.id
            left = (
                f"🤖 O bot foi removido do grupo {title} #GrupoRemovido\n"
                f"📋 **Nome do Chat**: {title}\n"
                f"🆔 **ID do Chat**: {chat_id}\n"
                f"🔗 **Nome de Usuário do Chat**: {username}\n"
                f"👤 **Removido Por**: {remove_by}"
            )

            await app.send_message(
                LOG_GROUP_ID,
                text=left,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text=f"Removido por: {message.from_user.first_name}",
                                user_id=message.from_user.id,
                            )
                        ]
                    ]
                ),
            )
            await delete_served_chat(chat_id)
            await userbot.leave_chat(chat_id)
    except Exception as e:
        pass
