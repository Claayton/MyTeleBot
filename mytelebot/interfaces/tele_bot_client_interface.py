"""Interface para a classe TeleBotClient"""
from abc import ABC, abstractmethod


class TeleBotClientInterface(ABC):
    """Interface para a classe TeleBotClient"""

    @abstractmethod
    def init_client(self):
        """Deve ser implementado"""

        raise Exception("Deve ser implementado o metodo: init_client")

    @abstractmethod
    def new_messages(self):
        """Deve ser implementado"""

        raise Exception("Deve ser implementado o metodo: get_new_messages")
