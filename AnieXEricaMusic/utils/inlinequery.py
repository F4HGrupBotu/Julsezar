from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            Başlık="ꜱᴛᴀʀᴛ",
            Açıklama="ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ",
            thumb_url="https://t.me/gozlerimuzikal/44",
            input_message_content=InputTextMessageContent("/start"),
        ),
        InlineQueryResultArticle(
            Başlık="ʜᴇʟᴘ",
            Açıklama="ᴄʜᴇᴄᴋ ʙᴏᴛ ᴄᴍᴅꜱ",
            thumb_url="https://t.me/gozlerimuzikal/44",
            input_message_content=InputTextMessageContent("/help"),
        ),
        InlineQueryResultArticle(
            Başlık="Pᴀᴜsᴇ",
            Açıklama=f"ᴩᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://t.me/gozlerimuzikal/44",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            Başlık="Rᴇsᴜᴍᴇ",
            Açıklama=f"ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴩᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://t.me/gozlerimuzikal/44",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            Başlık="Sᴋɪᴩ",
            Açıklama=f"sᴋɪᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ ᴀɴᴅ ᴍᴏᴠᴇs ᴛᴏ ᴛʜᴇ ɴᴇxᴛ sᴛʀᴇᴀᴍ.",
            thumb_url="https://t.me/gozlerimuzikal/44",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            Başlık="Eɴᴅ",
            Açıklama="ᴇɴᴅ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://t.me/gozlerimuzikal/44",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            Başlık="Sʜᴜғғʟᴇ",
            Açıklama="sʜᴜғғʟᴇ ᴛʜᴇ ǫᴜᴇᴜᴇᴅ sᴏɴɢs ɪɴ ᴩʟᴀʏʟɪsᴛ.",
            thumb_url="https://t.me/gozlerimuzikal/44",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            Başlık="Lᴏᴏᴩ",
            Açıklama="ʟᴏᴏᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ ᴛʀᴀᴄᴋ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://t.me/gozlerimuzikal/44",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
