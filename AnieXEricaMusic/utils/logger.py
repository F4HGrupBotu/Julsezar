from pyrogram.enums import ParseMode

from AnieXEricaMusic import app
from AnieXEricaMusic.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>{app.mention} ᴘʟᴀʏ ʟᴏɢ</b>
╔════❰𝐏𝐋𝐀𝐘𝐈𝐍𝐆❱═══❍⊱❁۪۪
<b>◈ 𝗦𝗢𝗛𝗕𝗘𝗧 ➪ </b>{message.chat.title}
<b>◈ 𝗦𝗢𝗛𝗕𝗘𝗧 𝗜𝗗 ➪ </b> <code>{message.chat.id}</code>
<b>◈ 𝗞𝗨𝗟𝗟𝗔𝗡𝗜𝗖𝗜 ➪ </b> {message.from_user.mention}
<b>◈ 𝗞𝗨𝗟𝗟𝗔𝗡𝗜𝗖𝗜 𝗔𝗗𝗜 ➪ </b> @{message.from_user.username}
<b>◈ 𝐈𝐝 ➪ </b> <code>{message.from_user.id}</code>
<b>◈ 𝗦𝗢𝗛𝗕𝗘𝗧 𝗟𝗜̇𝗡𝗞𝗜̇ ➪ </b> @{message.chat.username}
<b>◈ 𝙰𝚁𝙰𝙽𝙳𝙸 ➪ </b> <code>{message.text.split(None, 1)[1]}</code>
<b>◈ 𝗧𝗔𝗥𝗔𝗙𝗜𝗡𝗗𝗔𝗡 ➪ </b> {streamtype}
╚═══❰ #𝐍𝐞𝐰𝐒𝐨𝐧𝐠 ❱══❍⊱❁۪۪"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
