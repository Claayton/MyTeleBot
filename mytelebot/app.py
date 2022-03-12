"""App para receber e tratar mensagens do telegram"""
import os
from typing import Type
from telethon import TelegramClient, events


class MyTeleBot(TelegramClient):
    """Automatizacao para telegram"""

    def __init__(self, telegram_client: Type[TelegramClient]):

        self.__client = telegram_client

        self.__telegram_bot = None
        self.__my_self = None

    def init_app(
        self,
        api_id: int,
        api_hash: str,
        bot_token: str,
        session: any = os.environ.get("TG_SESSION", "printer"),
        proxy: any = None,
    ):
        """Inicializacao do bot"""

        client = self.__client(
            api_id=api_id, api_hash=api_hash, session=session, proxy=proxy
        )

        self.__telegram_bot = self.__client(
            api_id=api_id, api_hash=api_hash, session="bot", proxy=proxy
        )

        self.get_new_messages(client)

        client.start()
        print("\033[31m(Press Ctrl+C to stop this)\033[m")
        client.run_until_disconnected()

        self.__telegram_bot.start(bot_token=bot_token)
        self.__telegram_bot.run_until_disconnected()

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

            if sender.username != self.__my_self.username:

                if "python" in event.raw_text:

                    await client.send_message(
                        group,
                        f"""
                        Vaga nova guys!

                        Usuario: {sender.username}
                        Mensagem: {event.raw_text}
                        """,
                    )

                if "oi" in event.raw_text:
                    await self.send_bot_messages(
                        sender.username, "Oi, sou um bot de testes!"
                    )

                if "vsfd" in event.raw_text:
                    await self.send_bot_messages(sender.username, "Arrombado!")

    def send_bot_messages(self, user_group, message):
        "Enviando respostas pelo bot"

        with self.__telegram_bot.send_message as bot:

            bot.send_message(user_group, message)
