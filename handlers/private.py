# ❰ᴅᴇᴠɪʟ✘ᴍᴜsɪᴄ❱
# ❰ᴀᴅɪᴛʏᴀ✘ʜᴀʟᴅᴇʀ❱

from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/77c2fb5dd16ebf30ac356.png",
        caption=f"""<b>**❰ᴅᴇᴠɪʟ✘ᴍᴜsɪᴄ❱ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴍᴀxᴇᴅ\nsᴜᴘᴇʀғᴀsᴛ ᴀɴᴅ ʜɪɢʜ ǫᴜᴀʟɪᴛʏ ᴠᴄ ᴍᴜsɪᴄ\nᴘʟᴀʏᴇʀ ʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ [ᴅᴇᴠɪʟ ᴍᴀғɪᴀ](t.me/Devilmafia09) ...**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/devilvcbot?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(command(["start", f"start@devilvcbot"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/77c2fb5dd16ebf30ac356.png",
        caption=f"""<b>**❰ᴅᴇᴠɪʟ✘ᴍᴜsɪᴄ❱ sᴜᴘᴇʀ ғᴀsᴛ\nʜɪɢʜ ǫᴜᴀʟɪᴛʏ » ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ\nʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ [ᴅᴇᴠɪʟ ᴍᴀғɪᴀ](t.me/Devilmafia09) ...**
        </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴊᴏɪɴ ʜᴇʀᴇ ᴀɴᴅ sᴜᴘᴘᴏʀᴛ 💥", url=f"https://t.me/majelelo09")
                ]
            ]
        ),
    )


@Client.on_message(command(["help", f"help@devilvcbot"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/77c2fb5dd16ebf30ac356.png",
        caption=f"""<b>**❰ᴅᴇᴠɪʟ✘ᴍᴜsɪᴄ❱ sᴜᴘᴇʀ ғᴀsᴛ\nʜɪɢʜ ǫᴜᴀʟɪᴛʏ » ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ\nʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ [ᴅᴇᴠɪʟ ᴍᴀғɪᴀ](t.me/Devilmafia09) ...**
        </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴄʟɪᴄᴋ ʜᴇʀᴇ »» ғᴏʀ ᴍᴏʀᴇ 💞", url=f"https://t.me/devilXsupport09")
                ]
            ]
        ),
    )
