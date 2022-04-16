"""Realiza analise e filtragem de mensagens"""
import re
from typing import Type
from telethon.tl.types import User
from telethon.events import NewMessage
from mytelebot.config import API
from mytelebot.interfaces import MessageParserInterface


class MessageParser(MessageParserInterface):
    """
    Realiza a analise e filtragem de mensagens e decide qual a melhor resposta.
    """

    def __init__(self) -> None:

        self.__group = API["group"]

    def parse_message(
        self, myself: Type[User], sender: Type[User], event: Type[NewMessage.Event]
    ):
        """Analise e filtro de mensagens"""

        response = None

        if sender.username == myself.username:

            return None

        python_opportunity = self.__is_python_opportunity(event)

        if python_opportunity["success"]:

            response = {
                "success": True,
                "reply": False,
                "forward": True,
                "entity": self.__group,
                "message": python_opportunity["message"],
            }

        if event.message.message.lower() == "oi":

            response = {
                "success": True,
                "reply": True,
                "forward": False,
                "entity": sender.username,
                "message": "Oi, sou um bot de testes!",
            }

        if event.message.message.lower() == "noia":

            response = {
                "success": True,
                "reply": True,
                "forward": False,
                "entity": sender.username,
                "message": "Aloprado! (mensagem automatica)",
            }

        return response

    def words_filter(self, message: str):
        """Realiza a filtragem de palavras na mensagem"""

        message = message.lower()
        words_filter = re.compile("(oportunidade*|vaga*|vaguinha*|emprego*|trabalho*)")

        if re.search(words_filter, message):

            return True

        return False

    def __is_python_opportunity(self, event: Type[NewMessage.Event]):
        """Verifica se a mensagem é uma oportunidade de vaga python"""

        message = event.message.message.lower()

        python = re.compile("python")

        if re.search(python, message) is None:

            return {"success": False, "message": None}

        if self.words_filter(message):

            return {"success": True, "message": event.message.message}

        return {"success": False, "message": None}

    @classmethod
    def print_message(
        cls, myself: Type[User], sender: Type[User], event: Type[NewMessage.Event]
    ):
        """Printa na tela informações da mensagem"""

        print()
        print(f"\033[32mmensagem: \033[35m{event.message.message}\033[m")
        print(f"\033[34musername: \033[35m{sender.username}\033[m")
        print(f"\033[34muser_id: \033[35m{sender.id}\033[m")
        print(f"\033[34mSou eu?: \033[35m{sender.is_self}\033[m")
        print(f"\033[34mQuem sou eu?: \033[35m{myself.username}\033[m")
