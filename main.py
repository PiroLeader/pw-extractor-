import pyrogram
from pyrogram import Client, filters
from pyromod import listen
from pyrogram.types import Message
from pyrogram.types.messages_and_media import message
import time
import urllib
import urllib.parse
import tgcrypto
from pyrogram.types import User
import time
import os
import threading
import requests
import json
import re
#from Crypto.Cipher import AES
#from Crypto.Util.Padding import unpad
#from base64 import b64encode, b64decode

bot_token = os.environ.get("TOKEN", "6855105570:AAFcqA756t3CZzMwzwNM08fTeUFj9P8vBRI") 
api_hash = os.environ.get("HASH", "2034b81303744d1dd2c7ffc02e21cfe2") 
api_id = os.environ.get("ID", "18429621")

bot = Client("mybot",api_id=api_id,api_hash=api_hash,bot_token=bot_token)



@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
 editable = await m.reply_text("**I am /pw links extract bot**")

@bot.on_message(filters.command(["pw"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text(
        "Send **Auth code** in this manner otherwise bot will not respond.\n\nSend like this:-  **AUTH CODE**"
    )  
    input1: Message = await bot.listen(editable.chat.id)
    raw_text1=input1.text
    headers = {

            'Host': 'api.penpencil.xyz',

            'authorization': f"Bearer {raw_text1}",

            'client-id': '5eb393ee95fab7468a79d189',

            'client-version': '12.84',

            'user-agent': 'Android',

            'randomid': 'e4307177362e86f1',

            'client-type': 'MOBILE',

            'device-meta': '{APP_VERSION:12.84,DEVICE_MAKE:Asus,DEVICE_MODEL:ASUS_X00TD,OS_VERSION:6,PACKAGE_NAME:xyz.penpencil.physicswalb}',

            'content-type': 'application/json; charset=UTF-8',

        # 'content-length': '89',

        # 'accept-encoding': 'gzip' ,
    }

    params = {
       'mode': '1',
       'filter': 'false',
       'exam': '',
       'amount': '',
       'organisationId': '5eb393ee95fab7468a79d189',
       'classes': '',
       'limit': '20',
       'page': '1',
       'programId': '',
       'ut': '1652675230446', 
    }
    await editable.edit("**You have these Batches :-\n\nBatch ID : Batch Name**")
    response = requests.get('https://api.penpencil.xyz/v3/batches/my-batches', params=params, headers=headers).json()["data"]
    for data in response:
        batch=(data["name"])
        #batchId=(data["_id"])
        aa=f"`{data['name']}`  :  `{data['_id']}\n`"
        await m.reply_text(aa)
    #time.sleep(2)
    editable1 = await m.reply_text("**Now send the Batch ID to Download**")
input3 = await bot.listen(editable.chat.id)  # Assuming 'editable' is defined elsewhere
raw_text3 = input3.text

try:
    response2 = requests.get(f'https://api.penpencil.xyz/v3/batches/{raw_text3}/details', headers=headers).json()["data"]["subjects"]

    subject_info = ""
    for subject in response2:   
        subject_name = subject.get('subject', 'Subject Name Unavailable')  # Handle missing 'subject'
        subject_id = subject.get('_id', 'Subject ID Unavailable')  # Handle missing '_id'
        subject_info += f"**{subject_name}** : `{subject_id}`\n\n"

    await editable1.edit_text(subject_info)  # Update the message

except requests.exceptions.RequestException as e:
    await editable1.edit_text(f"Error getting subjects: {str(e)}")
except KeyError as e:
    await editable1.edit_text(f"Error in response format: {str(e)}")
    vj=""
    for data in response2:
       #topic=(data["subject"])
        #topic_id=(data["_id"])
        #idid=f"{topic_id}&"
        bb=f"{data['_id']}&"
        await m.reply_text(bb)
    vj=""
    for data in response2:
        tids = (data['_id'])
        idid=f"{tids}&"
        if len(f"{vj}{idid}")>4096:
            await m.reply_text(idid)
            vj = ""
        vj+=idid
    editable2= await m.reply_text("**Enter this to download full batch :-**\n```{vj}```")
    input4 = message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text
   
    try:
        xv = raw_text4.split('&')

        for y in range(0,len(xv)):
            t =xv[y]
            params1 = {'page': '1','tag': '','contentType': 'exercises-notes-videos','ut': ''}
            response3 = requests.get(f'https://api.penpencil.xyz/v2/batches/{raw_text3}/subject/{t}/contents', params=params1, headers=headers).json()["data"]
            
            params2 = {'page': '2','tag': '','contentType': 'exercises-notes-videos','ut': ''}
            response4 = requests.get(f'https://api.penpencil.xyz/v2/batches/{raw_text3}/subject/{t}/contents', params=params2, headers=headers).json()["data"]
            
            params3 = {'page': '3','tag': '','contentType': 'exercises-notes-videos','ut': ''}
            response5 = requests.get(f'https://api.penpencil.xyz/v2/batches/{raw_text3}/subject/{t}/contents', params=params3, headers=headers).json()["data"]
            
            params4 = {'page': '4','tag': '','contentType': 'exercises-notes-videos','ut': ''}
            response6 = requests.get(f'https://api.penpencil.xyz/v2/batches/{raw_text3}/subject/{t}/contents', params=params4, headers=headers).json()["data"]
            
            params5 = {'page': '5','tag': '','contentType': 'exercises-notes-videos','ut': ''}
            response7 = requests.get(f'https://api.penpencil.xyz/v2/batches/{raw_text3}/subject/{t}/contents', params=params4, headers=headers).json()["data"]
            
            params6 = {'page': '6','tag': '','contentType': 'exercises-notes-videos','ut': ''}
            response8 = requests.get(f'https://api.penpencil.xyz/v2/batches/{raw_text3}/subject/{t}/contents', params=params4, headers=headers).json()["data"]
            
            params7 = {'page': '7','tag': '','contentType': 'exercises-notes-videos','ut': ''}
            response9 = requests.get(f'https://api.penpencil.xyz/v2/batches/{raw_text3}/subject/{t}/contents', params=params4, headers=headers).json()["data"]
            
            params8 = {'page': '8','tag': '','contentType': 'exercises-notes-videos','ut': ''}
            response10 = requests.get(f'https://api.penpencil.xyz/v2/batches/{raw_text3}/subject/{t}/contents', params=params4, headers=headers).json()["data"]
            #await m.reply_text(response3)
            try:
                for data in response3:
                    class_title=(data["topic"])
                    class_url=data["url"].replace("d1d34p8vz63oiq", "d26g5bnklkwsh4").replace("mpd", "m3u8").strip()
                #cc=f"```{data['topic']}```:```{data['url']}\n```"
                    cc = f"{data['topic']}:{data['url']}"
                    with open(f"{batch}.txt", 'a') as f:
                        f.write(f"{class_title}:{class_url}\n")
                #await m.reply_text(cc)
                #await m.reply_document(f"{batch}.txt")
            except Exception as e:
               await m.reply_text(str(e))
            #await m.reply_document(f"{batch}.txt")
            try:
                for data in response4:
                    class_title=(data["topic"])
                    class_url=data["url"].replace("d1d34p8vz63oiq", "d26g5bnklkwsh4").replace("mpd", "m3u8").strip()
                #cc=f"```{data['topic']}```:```{data['url']}\n```"
                    cc = f"{data['topic']}:{data['url']}"
                    with open(f"{batch}.txt", 'a') as f:
                        f.write(f"{class_title}:{class_url}\n")
                #await m.reply_text(cc)
                #await m.reply_document(f"{batch}.txt")
            except Exception as e:
               await m.reply_text(str(e))
            #await m.reply_document(f"{batch}.txt")
            try:
                for data in response5:
                    class_title=(data["topic"])
                    class_url=data["url"].replace("d1d34p8vz63oiq", "d26g5bnklkwsh4").replace("mpd", "m3u8").strip()
                #cc=f"```{data['topic']}```:```{data['url']}\n```"
                    cc = f"{data['topic']}:{data['url']}"
                    with open(f"{batch}.txt", 'a') as f:
                     f.write(f"{class_title}:{class_url}\n")
                #await m.reply_text(cc)
                #await m.reply_document(f"{batch}.txt")
            except Exception as e:
               await m.reply_text(str(e))
            #await m.reply_document(f"{batch}.txt")
            try:
                for data in response6:
                    class_title=(data["topic"])
                    class_url=data["url"].replace("d1d34p8vz63oiq", "d26g5bnklkwsh4").replace("mpd", "m3u8").strip()
                #cc=f"```{data['topic']}```:```{data['url']}\n```"
                    cc = f"{data['topic']}:{data['url']}"
                    with open(f"{batch}.txt", 'a') as f:
                        f.write(f"{class_title}:{class_url}\n")
                #await m.reply_text(cc)
                #await m.reply_document(f"{batch}.txt")
            except Exception as e:
               await m.reply_text(str(e))
            try:
                for data in response7:
                    class_title=(data["topic"])
                    class_url=data["url"].replace("d1d34p8vz63oiq", "d26g5bnklkwsh4").replace("mpd", "m3u8").strip()
                #cc=f"```{data['topic']}```:```{data['url']}\n```"
                    cc = f"{data['topic']}:{data['url']}"
                    with open(f"{batch}.txt", 'a') as f:
                        f.write(f"{class_title}:{class_url}\n")
                #await m.reply_text(cc)
                #await m.reply_document(f"{batch}.txt")
            except Exception as e:
               await m.reply_text(str(e))
            #await m.reply_document(f"{batch}.txt")
            try:
                for data in response8:
                    class_title=(data["topic"])
                    class_url=data["url"].replace("d1d34p8vz63oiq", "d26g5bnklkwsh4").replace("mpd", "m3u8").strip()
                #cc=f"```{data['topic']}```:```{data['url']}\n```"
                    cc = f"{data['topic']}:{data['url']}"
                    with open(f"{batch}.txt", 'a') as f:
                        f.write(f"{class_title}:{class_url}\n")
                #await m.reply_text(cc)
                #await m.reply_document(f"{batch}.txt")
            except Exception as e:
               await m.reply_text(str(e))
            #await m.reply_document(f"{batch}.txt")
            try:
                for data in response9:
                    class_title=(data["topic"])
                    class_url=data["url"].replace("d1d34p8vz63oiq", "d26g5bnklkwsh4").replace("mpd", "m3u8").strip()
                #cc=f"```{data['topic']}```:```{data['url']}\n```"
                    cc = f"{data['topic']}:{data['url']}"
                    with open(f"{batch}.txt", 'a') as f:
                     f.write(f"{class_title}:{class_url}\n")
                #await m.reply_text(cc)
                #await m.reply_document(f"{batch}.txt")
            except Exception as e:
               await m.reply_text(str(e))
            #await m.reply_document(f"{batch}.txt")
            try:
                for data in response10:
                    class_title=(data["topic"])
                    class_url=data["url"].replace("d1d34p8vz63oiq", "d26g5bnklkwsh4").replace("mpd", "m3u8").strip()
                #cc=f"```{data['topic']}```:```{data['url']}\n```"
                    cc = f"{data['topic']}:{data['url']}"
                    with open(f"{batch}.txt", 'a') as f:
                        f.write(f"{class_title}:{class_url}\n")
                #await m.reply_text(cc)
                #await m.reply_document(f"{batch}.txt")
            except Exception as e:
               await m.reply_text(str(e))
            await m.reply_document(f"{batch}.txt")
    except Exception as e:
        await m.reply_text(str(e))

# infinty polling
bot.run()
