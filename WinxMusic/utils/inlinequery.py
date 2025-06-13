from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Pause Streaming",
            description="Pauses the music playing in voice chat.",
            thumb_url="https://telegra.ph/file/c0a1c789def7b93f13745.png",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="Resume Broadcast/Stream",
            description="Return to slow music in voice chat.",
            thumb_url="https://telegra.ph/file/02d1b7f967ca11404455a.png",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="Mute Transmission",
            description="Mutes the music playing in voice chat.",
            thumb_url="https://telegra.ph/file/66516f2976cb6d87e20f9.png",
            input_message_content=InputTextMessageContent("/vcmute"),
        ),
        InlineQueryResultArticle(
            title="Unmute Transmission",
            description="Unmutes the music playing in voice chat.",
            thumb_url="https://telegra.ph/file/3078794f9341ffd582e18.png",
            input_message_content=InputTextMessageContent("/vcunmute"),
        ),
        InlineQueryResultArticle(
            title="Skip Transmission",
            description="Skip to the next track. To skip to a specific track: /skip [number]",
            thumb_url="https://telegra.ph/file/98b88e52bc625903c7a2f.png",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="End Transmission",
            description="For the music playing in the group voice chat.",
            thumb_url="https://telegra.ph/file/d2eb03211baaba8838cc4.png",
            input_message_content=InputTextMessageContent("/stop"),
        ),
        InlineQueryResultArticle(
            title="Shuffle Transmission",
            description="Shuffles the list of songs in the queue.",
            thumb_url="https://telegra.ph/file/7f6aac5c6e27d41a4a269.png",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="Forward Transmission",
            description="Advances the music to a specific duration.",
            thumb_url="https://telegra.ph/file/cd25ec6f046aa8003cfee.png",
            input_message_content=InputTextMessageContent("/seek 10"),
        ),
        InlineQueryResultArticle(
            title="Repeat Broadcast",
            description="Repeats the current song. Usage: /loop [enable|disable]",
            thumb_url="https://telegra.ph/file/081c20ce2074ea3e9b952.png",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
