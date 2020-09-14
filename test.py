from pyrogram import Client
import asyncio


async def main():
    client=Client('+2347054467363')
    await client.start()
    async for dialog in client.iter_dialogs():
        chat=dialog.chat
        print(chat.type,chat.username if chat.username else chat.title,chat.id)
    await client.stop()


asyncio.get_event_loop().run_until_complete(main())
# git push https://borden-heroku:bordenheroku2.@github.com/borden-heroku/borden_userbot.git