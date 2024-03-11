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
       'amount': 'paid',
       'page': '1',
    }
       
    await editable.edit("**You have these Batches :-\n\nBatch ID : Batch Name**")
    response = requests.get('https://api.penpencil.xyz/v3/batches/my-batches', params=params, headers=headers).json()["data"]
    for data in response:
        batch=(data["name"])
        #batchId=(data["_id"])
        aa=f"`{data['name']}`  :  `{data['_id']}\n`"
        await m.reply_text(aa)
    #time.sleep(2)
    await m.reply_text("**You have these Batches :-\n\nBatch ID : Batch Name**")
    aa=''
    response = requests.get('https://api.penpencil.co/v3/batches/my-batches', params=params, headers=headers).json()["data"]
    for data in response:
        batch_name = data['name']
        batch_id = data['_id']
        aa = aa + f'**{batch_name}**  :  ```{batch_id}```\n\n'
    await m.reply_text(aa)
    editable1= await m.reply_text("**Now send the Batch ID to Download**")
    input3 = message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    response2 = requests.get(f'https://api.penpencil.co/v3/batches/{raw_text3}/details', headers=headers).json()["data"]["subjects"]
    await m.reply_text("Subject : Subject_Id")
    bb= ''
    for data in response2:
        subject_name = data['subject']
        subject_id = data['_id']
        bb = bb  + f'**{subject_name}**  :  ```{subject_id}```\n\n'
    await m.reply_text(bb)
    raw_text3 = input3.text
    response2 = requests.get(f'https://api.penpencil.co/v3/batches/{raw_text3}/details', headers=headers).json()["data"]["subjects"]
    await m.reply_text("Subject : Subject_Id")
    bb= ''
    for data in response2:
        subject_name = data['subject']
        subject_id = data['_id']
        bb = bb  + f'**{subject_name}**  :  ```{subject_id}```\n\n'
    await m.reply_text(bb)
    editable2= await m.reply_text("**Now send the subject ID to Download**")
    input4 = message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text
    await m.reply_text('**Now Send Content Type you want to extract.**\n```DppNotes```|```videos```|```notes```')
    input5 = message = await bot.listen(editable.chat.id)
    raw_text5 = input5.text
    xx =await m.reply_text("Genrating Course txt in this id")
    to_write = ''
    for z in range(1,15): # max 15 pages
        print(z) 
        params1 = {
        'page': f'{z}',
        'tag': '',
        'contentType': f'{raw_text5}',
        }
        
        response3 = requests.get(f'https://api.penpencil.co/v2/batches/{raw_text3}/subject/{raw_text4}/contents', params=params1, headers=headers).json()["data"]
        #with open(f"1pwnotes.json", "w", encoding="utf-8") as f:
        #    f.write(f'{response3}')
        #    print(1)
        #    sys.exit(1)
        
        if raw_text5 == 'videos':
            for data in response3:
                try:      
                    url = f"https://d26g5bnklkwsh4.cloudfront.net/{data['url'].split('/')[-2]}/hls/720/main.m3u8" if raw_text5 == "videos" else f"{data['baseUrl']}{data['key']}"
                    topic = data['topic']
                    #print(url)
                    write = f"{topic} {url}\n"
                    to_write = to_write + write
                except:
                    pass
        else: #for notes + dpps
            for i in range(len(response3)):
                #print(response3)
                #print(data1)
                try:
                    print(f'{i} {z} ')
                    c=response3[i]
                    b=c['homeworkIds'][0]
                    a = b['attachmentIds'][0]
                
                    #print(f'{b}')
                    name = response3[i]['homeworkIds'][0]['topic'].replace('|',' ').replace(':',' ')
                    #name = a['name']
                    url = a['baseUrl'] + a['key']
                    write = f"{name} {url}\n"
                    to_write = to_write + write
                except:
                    pass

    with open(f"{raw_text5} {raw_text4}.txt", "w", encoding="utf-8") as f:
        f.write(to_write)
        print(1)
    with open(f"{raw_text5} {raw_text4}.txt", "rb") as f:   
       # print(3)  
        await asyncio.sleep(5)
        doc = await message.reply_document(document=f, caption="Here is your txt file.")
        await xx.delete(True)
       # print(2)
    await bot.forward_messages(acces,doc.chat.id,doc.message_id) 

# infinty polling
bot.run()
