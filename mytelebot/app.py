"""App para receber e tratar mensagens do telegram"""
import os
from typing import Type
from telethon import TelegramClient, events
from telethon.tl.types import PeerChat, PeerUser


class MyTeleBot(TelegramClient):
    """Automatizacao para telegram"""

    def __init__(
        self,
        telegram_client: Type[TelegramClient],
        api_id: int,
        api_hash: str,
        bot_token: str,
        session: any = os.environ.get("TG_SESSION", "printer"),
        proxy: any = None,
    ):

        self.__client = telegram_client(
            api_id=api_id, api_hash=api_hash, session=session, proxy=proxy
        )
        self.__bot_token = bot_token
        self.__my_self = None

    def init_client(self):
        """Inicializacao do bot"""

        self.get_new_messages(self.__client)

        self.__client.start()
        print("\033[31m(Press Ctrl+C to stop this client!)\033[m")
        self.__client.run_until_disconnected()

    def get_new_messages(self, client: Type[TelegramClient]):
        """Recebe eventos de mensagens no telegram."""

        @client.on(events.NewMessage)
        async def handler(event):
            """Identificar atualizacoes no servidor"""

            sender = await event.get_sender()
            group = 732536148
            self.__my_self = await client.get_me()

            print(event)
            print()
            print(f"\033[32mmensagem: \033[35m{event.raw_text}\033[m")
            print(f"\033[34musername: \033[35m{sender.username}\033[m")
            print(f"\033[34muser_id: \033[35m{sender.id}\033[m")
            print(f"\033[34mSou eu?: \033[35m{sender.is_self}\033[m")

            if sender.username == self.__my_self.username:

                if "python" in event.raw_text:

                    await client.send_message(
                        PeerChat(group),
                        f"""
                        Vaga nova guys!

                        Usuario: {sender.username}
                        Mensagem: {event.raw_text}
                        """,
                    )

                if "oi" in event.raw_text:

                    await event.reply("Oi, sou um bot de testes!")

                if "vsfd" in event.raw_text:

                    await event.reply("Arrombado!")
