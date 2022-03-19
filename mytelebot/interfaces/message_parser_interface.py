"""Interface para a classe MessageParser"""
from abc import ABC, abstractmethod
from typing import Type, List
from telethon.tl.types import User
from telethon.events import NewMessage


class MessageParserInterface(ABC):
    """Interface para a classe MessageParser"""

    @abstractmethod
    def parse_message(
        self, myself: Type[User], sender: Type[User], event: Type[NewMessage.Event]
    ):
        """Deve ser implementado"""

        raise Exception("Deve ser implementado o metodo: parse_message")

    @classmethod
    @abstractmethod
    def words_filter(cls, message: List):
        """Deve ser implementado"""

        raise Exception("Deve ser implementado o metodo: words_filter")
