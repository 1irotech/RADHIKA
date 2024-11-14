from config import OWNER_USERNAME, SUPPORT_GRP
from RADHIKA import RADHIKA
from pyrogram import Client, filters



START = """**
{} ᴛʜᴇ ꜱᴜᴘᴇʀғᴀꜱᴛ ᴄʜᴀᴛʙᴏᴛ 💞

➪ ꜱᴜᴘᴘᴏʀᴛꜱ ᴛᴇxᴛ, ꜱᴛɪᴄᴋᴇʀ, ᴘʜᴏᴛᴏ, ᴠɪᴅᴇᴏ...
➪ ᴍᴜʟᴛɪ-ʟᴀɴɢᴜᴀɢᴇ ғᴏʀ ᴇᴀᴄʜ ᴄʜᴀᴛ /lang
➪ ᴄʜᴀᴛʙᴏᴛ ᴇɴᴀʙʟᴇᴅ/ᴅɪꜱᴀʙʟᴇᴅ ʙʏ /chatbot
➪ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ᴄʜᴀᴛʙᴏᴛ ʙʏ /clone

๏ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ : {}
๏ ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ : {}
๏ ᴜᴘᴛɪᴍᴇ » {}

╔═════════════════╗
║ ➻ ᴍʏ ʀᴇᴘᴏ ➪ [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/THE-VIP-BOY-OP/VIP-CHATBOT)  
║ ➻ ᴄʀᴇᴀᴛᴏʀ ➪ [ᴠɪᴘ ✯ ʙᴏʏ](https://t.me/the_vip_boy)                         
╚═════════════════╝
**"""

HELP_READ = f"""**
Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.  Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/THE_VIP_BOY).

Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /**
"""

TOOLS_DATA_READ = f"""**
๏ ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ᴛᴏᴏʟꜱ:

➻ /start ᴛᴏ ᴡᴀᴋᴇ ᴜᴘ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ʀᴇᴄᴇɪᴠᴇ ᴀ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ!
──────────────
➻ /help ғᴏʀ ɢᴇᴛᴛɪɴɢ ᴅᴇᴛᴀɪʟs ᴀʙᴏᴜᴛ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ғᴇᴀᴛᴜʀᴇs.
──────────────
➻ /ping ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ʀᴇsᴘᴏɴsᴇ ᴛɪᴍᴇ (ᴘɪɴɢ) ᴏғ ᴛʜᴇ ʙᴏᴛ!
──────────────
➻ /id ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴜsᴇʀ ɪᴅ, ᴄʜᴀᴛ ɪᴅ, ᴀɴᴅ ᴍᴇssᴀɢᴇ ɪᴅ ᴀʟʟ ɪɴ ᴏɴᴇ ᴍᴇssᴀɢᴇ.
──────────────
➻ /broadcast ᴛᴏ ғᴏʀᴡᴀʀᴅ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄʜᴀᴛs ʙᴀsᴇᴅ ᴏɴ sᴘᴇᴄɪғɪᴇᴅ ғʟᴀɢs!\nᴇxᴀᴍᴘʟᴇ: `/broadcast -user -pin ʜᴇʟʟᴏ ғʀɪᴇɴᴅs`
──────────────
➻ /shayri ɢᴇᴛ ʀᴀɴᴅᴏᴍ sʜᴀʏʀɪ ғᴏʀ ʏᴏᴜʀ ʟᴏᴠᴇ
──────────────
➻ /link (ɢʀᴏᴜᴩ ɪᴅ) ᴛᴏ ɢᴇᴛ ʟɪɴᴋ ᴏꜰ ɢʀᴏᴜᴩ
➻ /givelink ᴛᴏ ɢᴇᴛ ᴛʜᴀᴛ ɢʀᴏᴜᴩ ʟɪɴᴋ ɪɴ ᴡʜɪᴄʜ ᴄᴏᴍᴍᴀɴᴅ ɪꜱ ᴡʀɪᴛᴛᴇɴ (ᴡʀɪᴛᴇ ɪɴ ɢʀᴏᴜᴩ)
──────────────
➻ ᴜsᴇ /repo ᴛᴏ ɢᴇᴛ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴏғ ᴛʜᴇ ʙᴏᴛ!
──────────────
๏ ᴍᴀᴅᴇ ʙʏ ➪ [ᴠɪᴘ ✯ ʙᴏʏ](https://t.me/the_vip_boy) 💞**
"""

CHATBOT_READ = f"""**
๏ ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ᴄʜᴀᴛʙᴏᴛ:

➻ /chatbot - ᴏᴘᴇɴs ᴏᴘᴛɪᴏns ᴛᴏ ᴇɴᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ ᴛʜᴇ ᴄʜᴀᴛʙᴏᴛ.
──────────────
➻ /lang, /language, /setlang - ᴏᴘᴇɴs ᴀ ᴍᴇɴᴜ ᴛᴏ sᴇʟᴇᴄᴛ ᴛʜᴇ ᴄʜᴀᴛ ʟᴀɴɢᴜᴀɢᴇ.  
──────────────
➻ /resetlang, /nolang - ʀᴇsᴇᴛs ᴛʜᴇ ʙᴏᴛ's ʟᴀɴɢᴜᴀɢᴇ ᴛᴏ ᴍɪxᴇᴅ ʟᴀɴɢᴜᴀɢᴇ.
──────────────
/status - ᴄʜᴇᴄᴋ ᴄʜᴀᴛʙᴏᴛ ᴀᴄᴛɪᴠᴇ ᴏʀ ɴᴏᴛ.
──────────────
➻ /stats - ɢᴇᴛ ʙᴏᴛ ꜱᴛᴀᴛꜱ
──────────────
📡 ᴍᴀᴅᴇ ʙʏ ➪ [ᴠɪᴘ ✯ ʙᴏʏ](https://t.me/the_vip_boy) 💞**
"""

SOURCE_READ = f"**ʜᴇʏ, ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴏғ [{RADHIKA.name}](https://t.me/{RADHIKA.username}) ɪs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.**\n**ᴘʟᴇᴀsᴇ ғᴏʀᴋ ᴛʜᴇ ʀᴇᴘᴏ & ɢɪᴠᴇ ᴛʜᴇ sᴛᴀʀ ✯**\n**──────────────────**\n**ʜᴇʀᴇ ɪs ᴛʜᴇ [sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ](https://github.com/THE-VIP-BOY-OP/VIP-CHATBOT)**\n**──────────────────**\n**ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ ᴀᴛ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/{SUPPORT_GRP}).\n<b>||📡 ᴍᴀᴅᴇ ʙʏ ➪ [ᴠɪᴘ ✯ ʙᴏʏ](https://t.me/the_vip_boy) 💞**||</b>"

ADMIN_READ = f"sᴏᴏɴ"

ABOUT_READ = f"""
**➻ [{RADHIKA.name}](https://t.me/{RADHIKA.username}) ɪs ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛ-ʙᴏᴛ.**
**➻ [{RADHIKA.name}](https://t.me/{RADHIKA.username}) ʀᴇᴘʟɪᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴛᴏ ᴀ ᴜsᴇʀ.**
**➻ ʜᴇʟᴘs ʏᴏᴜ ɪɴ ᴀᴄᴛɪᴠᴀᴛɪɴɢ ʏᴏᴜʀ ɢʀᴏᴜᴘs.**
**➻ ᴡʀɪᴛᴛᴇɴ ɪɴ [ᴘʏᴛʜᴏɴ](https://www.python.org) ᴡɪᴛʜ [ᴍᴏɴɢᴏ-ᴅʙ](https://www.mongodb.com) ᴀs ᴀ ᴅᴀᴛᴀʙᴀsᴇ**
**──────────────**
**➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʙᴀsɪᴄ ʜᴇʟᴩ ᴀɴᴅ ɪɴғᴏ ᴀʙᴏᴜᴛ [{RADHIKA.name}](https://t.me/{RADHIKA.username})**
"""