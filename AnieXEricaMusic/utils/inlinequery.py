from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            Başlık="ꜱᴛᴀʀᴛ",
            Açıklama="ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ",
            thumb_url="https://t.me/gozlerimuzikal/44",
            input_message_content=InputTextMessageContent("/başlat"),
        ),
        InlineQueryResultArticle(
            Başlık="ʜᴇʟᴘ",
            Açıklama="ᴄʜᴇᴄᴋ ʙᴏᴛ ᴄᴍᴅꜱ",
            thumb_url="https://t.me/gozlerimuzikal/44",
            input_message_content=InputTextMessageContent("/yardım"),
        ),
        InlineQueryResultArticle(
            Başlık="Pᴀᴜsᴇ",
            Açıklama=f"ᴩᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://t.me/gozlerimuzikal/44",
            input_message_content=InputTextMessageContent("/duraklat"),
        ),
        InlineQueryResultArticle(
            Başlık="Rᴇsᴜᴍᴇ",
            Açıklama=f"ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴩᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://t.me/gozlerimuzikal/44",
            input_message_content=InputTextMessageContent("/devam"),
        ),
        InlineQueryResultArticle(
            Başlık="Sᴋɪᴩ",
            Açıklama=f"sᴋɪᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ ᴀɴᴅ ᴍᴏᴠᴇs ᴛᴏ ᴛʜᴇ ɴᴇxᴛ sᴛʀᴇᴀᴍ.",
            thumb_url="https://t.me/gozlerimuzikal/44",
            input_message_content=InputTextMessageContent("/atla"),
        ),
        InlineQueryResultArticle(
            Başlık="Eɴᴅ",
            Açıklama="ᴇɴᴅ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://t.me/gozlerimuzikal/44",
            input_message_content=InputTextMessageContent("/dur"),
        ),
        InlineQueryResultArticle(
            Başlık="Sʜᴜғғʟᴇ",
            Açıklama="sʜᴜғғʟᴇ ᴛʜᴇ ǫᴜᴇᴜᴇᴅ sᴏɴɢs ɪɴ ᴩʟᴀʏʟɪsᴛ.",
            thumb_url="https://t.me/gozlerimuzikal/44",
            input_message_content=InputTextMessageContent("/karıştır"),
        ),
        InlineQueryResultArticle(
            Başlık="Lᴏᴏᴩ",
            Açıklama="ʟᴏᴏᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ ᴛʀᴀᴄᴋ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://t.me/gozlerimuzikal/44",
            input_message_content=InputTextMessageContent("/döngü 3"),
        ),
    ]
)
