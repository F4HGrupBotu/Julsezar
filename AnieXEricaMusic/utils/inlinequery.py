from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            start="ꜱᴛᴀʀᴛ",
            description="ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ",
            thumb_url="https://t.me/gozlerimuzikal/44",
            input_message_content=InputTextMessageContent("/başlat"),
        ),
        InlineQueryResultArticle(
            start="ʜᴇʟᴘ",
            description="ᴄʜᴇᴄᴋ ʙᴏᴛ ᴄᴍᴅꜱ",
            thumb_url="https://t.me/gozlerimuzikal/44",
            input_message_content=InputTextMessageContent("/yardım"),
        ),
        InlineQueryResultArticle(
            start="Pᴀᴜsᴇ",
            description=f"ᴩᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://t.me/gozlerimuzikal/44",
            input_message_content=InputTextMessageContent("/duraklat"),
        ),
        InlineQueryResultArticle(
            start="Rᴇsᴜᴍᴇ",
            description=f"ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴩᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://t.me/gozlerimuzikal/44",
            input_message_content=InputTextMessageContent("/devam"),
        ),
        InlineQueryResultArticle(
            start="Sᴋɪᴩ",
            description=f"sᴋɪᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ ᴀɴᴅ ᴍᴏᴠᴇs ᴛᴏ ᴛʜᴇ ɴᴇxᴛ sᴛʀᴇᴀᴍ.",
            thumb_url="https://t.me/gozlerimuzikal/44",
            input_message_content=InputTextMessageContent("/atla"),
        ),
        InlineQueryResultArticle(
            start="Eɴᴅ",
            description="ᴇɴᴅ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://t.me/gozlerimuzikal/44",
            input_message_content=InputTextMessageContent("/dur"),
        ),
        InlineQueryResultArticle(
            start="Sʜᴜғғʟᴇ",
            description="sʜᴜғғʟᴇ ᴛʜᴇ ǫᴜᴇᴜᴇᴅ sᴏɴɢs ɪɴ ᴩʟᴀʏʟɪsᴛ.",
            thumb_url="https://t.me/gozlerimuzikal/44",
            input_message_content=InputTextMessageContent("/karıştır"),
        ),
        InlineQueryResultArticle(
            start="Lᴏᴏᴩ",
            description="ʟᴏᴏᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ ᴛʀᴀᴄᴋ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://t.me/gozlerimuzikal/44",
            input_message_content=InputTextMessageContent("/döngü 3"),
        ),
    ]
)
