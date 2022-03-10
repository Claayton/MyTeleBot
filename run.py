"""Script para rodar o projeto"""
from televagas.received_message import client

if __name__ == "__main__":
    client.start()
    client.run_until_disconnected()
