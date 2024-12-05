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
║ ➻ ᴍʏ ʀᴇᴘᴏ ➪ [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/)  
║ ➻ ᴄʀᴇᴀᴛᴏʀ ➪ [ᴠɪᴘ ✯ ʙᴏʏ](https://t.me/Ironmanhindigaming)                         
╚═════════════════╝
**"""

HELP_READ = f"""**
Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.  Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/Ironmanhindigaming).

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
๏ ᴍᴀᴅᴇ ʙʏ ➪ [ᴠɪᴘ ✯ ʙᴏʏ](https://t.me/Ironmanhindigaming) 💞**
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
📡 ᴍᴀᴅᴇ ʙʏ ➪ [ᴠɪᴘ ✯ ʙᴏʏ](https://t.me/Ironmanhindigaming) 💞**
"""

SOURCE_READ = f"REPO PAID H \n AP BATAE CASH DENA PASAND KREGE YA APNI EK KIDN€Y TENSION MAT LO KIDN€Y GHAR ME AAKE BHI NIKAL SAKTE H OR UPI CASH ALSO H"

ADMIN_READ = f"sᴏᴏɴ"

ABOUT_READ = f"""
**➻ [{RADHIKA.name}](https://t.me/{RADHIKA.username}) ɪs ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛ-ʙᴏᴛ.**
**➻ [{RADHIKA.name}](https://t.me/{RADHIKA.username}) ʀᴇᴘʟɪᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴛᴏ ᴀ ᴜsᴇʀ.**
**➻ ʜᴇʟᴘs ʏᴏᴜ ɪɴ ᴀᴄᴛɪᴠᴀᴛɪɴɢ ʏᴏᴜʀ ɢʀᴏᴜᴘs.**
**➻ ᴡʀɪᴛᴛᴇɴ ɪɴ [ᴘʏᴛʜᴏɴ](https://www.python.org) ᴡɪᴛʜ [ᴍᴏɴɢᴏ-ᴅʙ](https://www.mongodb.com) ᴀs ᴀ ᴅᴀᴛᴀʙᴀsᴇ**
**──────────────**
**➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʙᴀsɪᴄ ʜᴇʟᴩ ᴀɴᴅ ɪɴғᴏ ᴀʙᴏᴜᴛ [{RADHIKA.name}](https://t.me/{RADHIKA.username})**
"""
