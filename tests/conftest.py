"""Arquivo para fixtures"""
from pytest import fixture
from faker import Faker
from telethon.tl.types import User
from mytelebot.parser import MessageParser


fake = Faker()


@fixture
def parser():
    """Montando o objeto parse"""

    return MessageParser()


@fixture
def myself():
    """Montando objetos myself"""

    return User(id=fake.random_number(), username=fake.name())


@fixture
def sender(myself):  # pylint: disable=W0621
    """Montando objetos sender"""

    return User(id=fake.random_number(), username=fake.name())
