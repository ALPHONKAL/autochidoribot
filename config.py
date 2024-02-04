import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "") #⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "") #⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") #⚠️ Required
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","Snow_User_Data")     
    DB_URL  = os.environ.get("DB_URL","") #⚠️ Required
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()] #⚠️ Required
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") #⚠️ Required Username without @
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "")) #⚠️ Required
    FLOOD = int(os.environ.get("FLOOD", '10'))
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))



class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hᴇʟʟᴏ {} 👋,

<b>Tʜɪs ɪs ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ʏᴇᴛ ᴘᴏᴡᴇʀғᴜʟ ʀᴇɴᴀᴍᴇ ʙᴏᴛ.
Usɪɴɢ ᴛʜɪs ʙᴏᴛ ʏᴏᴜ ᴄᴀɴ ʀᴇɴᴀᴍᴇ ᴀɴᴅ ᴄʜᴀɴɢᴇ ᴛʜᴇ ᴛʜᴜᴍʙɴᴀɪʟ ᴏғ ʏᴏᴜʀ ғɪʟᴇ. Yᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴄᴏɴᴠᴇʀᴛ ᴠɪᴅᴇᴏ ᴛᴏ ғɪʟᴇ & ғɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ. Tʜɪs ʙᴏᴛ ᴀʟsᴏ sᴜᴘᴘᴏʀᴛs ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ

⚡️Pʀᴇsᴇɴᴛᴇᴅ Bʏ - @Animemoviesr</b>"""

    ABOUT_TXT = """<b>🤖 My Name: {}
    
I ᴀᴍ Dᴇᴠᴇʟᴏᴘᴇᴅ ғᴏʀ Fɪʟᴇ Oᴘᴇʀᴀᴛɪᴏɴ ᴜᴘᴛᴏ 𝟸GB ᴏɴ Tᴇʟᴇɢʀᴀᴍ.</b>
```BOT CONFIGURATION
○ Dᴏᴡɴʟᴏᴀᴅ Sᴘᴇᴇᴅ : 3-4 MB/s
○ Uᴘʟᴏᴀᴅ Sᴘᴇᴇᴅ : 3-4 MB/s
○ Pᴀʀᴀʟʟᴇʟ Pʀᴏᴄᴇss : Only 01
○ Usᴇʀ Tʏᴘᴇ : FREE
○ Tᴀsᴋ Hᴀɴᴅʟɪɴɢ : Smoothly < 800MB```
    <b>Mʏ Dᴀᴛᴀʙᴀsᴇ, Lɪʙʀᴀʀʏ, Sᴇʀᴠᴇʀ, Sᴏᴜʀᴄᴇ Cᴏᴅᴇs ᴅᴇᴛᴀɪʟs ᴀʀᴇ Rᴇsᴛʀɪᴄᴛᴇᴅ ʙʏ ᴍʏ Oᴡɴᴇʀ.Iғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴋɴᴏᴡ ᴛʜᴇɴ ᴀsᴋ Mʏ Oᴡɴᴇʀ: @Shidoteshika1</b>"""

    HELP_TXT = """
🌌 <b>HOW TO SET THUMBNILE</b>
  
‣ /start the BOT and send any photo to automatically set thumbnile
‣ /del_thumb - Delete your old thumbnile
‣ /view_thumb - View your current thumbnile

📑 <b>HOW TO SET CUSTOM CAPTION</b>

‣ /set_caption - Set a custom caption
‣ /see_caption - View your caption
‣ /del_caption - Delete your caption

Example:- /set_caption `📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}`

✏️ <b>HOW TO RENAME A FILE</b>

‣ new_file_name.extension
Send any file and type new file name \nAnd select the format [ document, video, audio ].

Example:- `E01 Solo Leveling (480p) ESUB [∞].mkv`
"""


    PROGRESS_BAR = f"""<b>
    
‣ 🗃️ Sɪᴢᴇ: {1} | {2}
‣ ⏳️ Dᴏɴᴇ : {0}%
‣ 🚀 Sᴩᴇᴇᴅ: {3}/s
‣ ⏰️ Eᴛᴀ: {4}
</b>
```RENAMED FILE:\n{new_filename}```
**⚡️Pᴏᴡᴇʀᴇᴅ Bʏ - @Animemoviesr**"""
