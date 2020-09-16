from typing import List
import asyncio
from pyrogram import Client,idle
from pyrogram.handlers import MessageHandler
from pyrogram import filters
from configparser import ConfigParser
from pyrogram.errors import UserNotParticipant
from pyrogram.types import Message,User
from random import shuffle


async def invite_people(client: Client,message: Message):
    from_group,to_group,max_number=message.command[1].strip('@'),\
                               message.command[2].strip('@'),\
                               min(50,int(message.command[3]))
    try:
        added=0
        members=await client.get_chat_members(from_group,200)
        shuffle(members)
        for member in members:
            user: User=member.user
            if user.is_bot:
                continue
            try:
                await client.get_chat_member(from_group,user.id)
            except UserNotParticipant:
                try:
                    await client.add_chat_members(to_group,user.id)
                except Exception as e:
                    print(e)
                    continue
                added+=1
            if added>=max_number:
                break
        await message.reply_text(f'Added {added} members from @{from_group} to @{to_group}')
    except Exception as e:
        await message.reply_text(str(e))


async def main(sessions: List[str]):
    clients: List[Client]=list()
    for session in sessions:
        clients.append(client:=Client(session,phone_number=session))
        client.add_handler(MessageHandler(invite_people,filters.command('add')))
        await client.start()
    await idle()


config=ConfigParser()
config.read('config.ini')
asyncio.get_event_loop().run_until_complete(main(config['adder']['sessions'].split()))
