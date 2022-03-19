"""Administracao de client para telegram"""
import os
from typing import Type, Union
from telethon import TelegramClient, events
from telethon.sessions.abstract import Session
from telethon.tl.types import PeerChat
from mytelebot.interfaces import TeleBotClientInterface, MessageParserInterface


class TeleBotClient(TeleBotClientInterface, TelegramClient):
    """Classe para administracao de client telegram"""

    def __init__(
        self,
        parser: Type[MessageParserInterface],
        api_id: int,
        api_hash: str,
        session: Union[str, Session] = os.environ.get("TG_SESSION", "printer"),
    ):

        super().__init__(session, api_id, api_hash)
        self.__parser = parser

    def init_client(self):
        """Inicializacao do bot"""

        self.get_new_messages()

        self.start()
        print("\033[31m(Press Ctrl+C to stop this client!)\033[m")
        self.run_until_disconnected()

    def get_new_messages(self):
        """Recebe eventos de mensagens no telegram"""

        @self.on(events.NewMessage)
        async def handler(event):
            """Identificar atualizacoes no servidor"""

            sender = await event.get_sender()
            myself = await self.get_me()

            response = self.__parser.parse_message(myself, sender, event)
            self.__parser.print_message(myself, sender, event)

            if not response:

                pass

            elif response["reply"]:

                await event.reply(response["message"])

            elif response["forward"]:

                await self.send_message(
                    PeerChat(int(response["entity"])), response["message"]
                )
