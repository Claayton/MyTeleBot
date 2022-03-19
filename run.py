"""Script para rodar o projeto"""
import asyncio
from mytelebot.client import TeleBotClient
from mytelebot.parser import MessageParser
from mytelebot.config import API


parser = MessageParser()
tele_bot = TeleBotClient(parser, api_id=API["api_id"], api_hash=API["api_hash"])

if __name__ == "__main__":

    asyncio.run(tele_bot.init_client())
