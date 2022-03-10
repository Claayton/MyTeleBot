"""App para receber e tratar mensagens do telegram"""
import os
from telethon import TelegramClient, events
from .config import API

session = os.environ.get("TG_SESSION", "printer")
PROXY = None

client = TelegramClient(session, API["api_id"], API["api_hash"])


@client.on(events.NewMessage)
async def handler(event):
    """Identificar atualizacoes no servidor"""

    sender = await event.get_sender()
    my_self = await client.get_me()

    print()
    print(f"\033[32mmensagem: \033[35m{event.raw_text}\033[m")
    print(f"\033[34musername: \033[35m{sender.username}\033[m")
    print(f"\033[34muser_id: \033[35m{sender.id}\033[m")
    print(f"\033[34mSou eu?: \033[35m{sender.is_self}\033[m")

    if sender.username != my_self.username:

        await client.send_message(
            "jair_messias_bot",
            f"""
            mensagem: {event.raw_text}
            username: {sender.username}
            user_id: {sender.id}
            Sou eu?: {sender.is_self}
            """,
        )

    if "Tem que se foder e acabou!" in event.raw_text:
        await event.reply("eae maluco")


# with TelegramClient(session, API["api_id"], API["api_hash"], proxy=proxy) as client:
#     # Register the update handler so that it gets called
#     client.add_event_handler(handler)

#     # Run the client until Ctrl+C is pressed, or the client disconnects
#     print('(Press Ctrl+C to stop this)')
#     client.run_until_disconnected()
