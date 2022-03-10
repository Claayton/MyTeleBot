# """Envio de mensagens"""
# import asyncio
# from telethon import TelegramClient
# from .config import API


# async def main():
#     """funçao de envio de mensagens"""

#     client = TelegramClient("session_name", API["api_id"], API["api_hash"])
#     await client.start()

#     print((await client.get_me()).stringify())

#     await client.send_message("jair_messias_bot", "Hello! Talking to you from Telethon")
#     # await client.send_file('username', '/home/myself/Pictures/holidays.jpg')

#     # await client.download_profile_photo('me')
#     messages = await client.get_messages("jair_messias_bot")
#     # await messages[0].download_media()

#     @client.on(events.NewMessage(pattern="(?i)hi|hello"))
#     async def handler(event):
#         await event.respond("Hey!")


# asyncio.run(main())
