from pyrogram import Client
import asyncio


async def main():
    client=Client('+2349067976861')
    await client.start()
    await client.stop()


asyncio.get_event_loop().run_until_complete(main())
# git push https://borden-heroku:bordenheroku2.@github.com/borden-heroku/borden_userbot.git