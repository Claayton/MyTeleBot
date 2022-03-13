"""Script para rodar o projeto"""
import asyncio
from telethon import TelegramClient
from mytelebot.config import API
from mytelebot import MyTeleBot


my_self_bot = MyTeleBot(TelegramClient, api_id=API["api_id"], api_hash=API["api_hash"])

if __name__ == "__main__":

    asyncio.run(my_self_bot.init_client())
