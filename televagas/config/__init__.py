"""Arquivo de configuracoes do projeto"""
import os
from dotenv import load_dotenv

load_dotenv()

API = {"api_id": os.getenv("API_ID"), "api_hash": os.getenv("API_HASH")}
