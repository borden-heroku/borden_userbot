from pyrogram import Client
import asyncio


async def main():
    client=Client('+2347054467363')
    await client.start()
    print(await client.get_chat_member('sqmonitor_chat',(await client.get_me()).id))
    await client.stop()


asyncio.get_event_loop().run_until_complete(main())
# git push https://borden-heroku:bordenheroku2.@github.com/borden-heroku/borden_userbot.git