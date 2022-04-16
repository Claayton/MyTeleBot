"""Testes para a classe MessageParser"""
from pytest import mark
from faker import Faker
from telethon.tl.types import User, Message, PeerUser
from telethon.events import NewMessage
from mytelebot.config import API


fake = Faker()


def test_parse_message_where_the_message_is_from_the_user(parser, myself):
    """
    Testando o metodo parse_message, onde a mensagem vem do proprio usuario.
    O sistema deve retornar None.
    """

    sender = User(id=fake.random_number(), username=myself.username)
    event = NewMessage.Event(
        Message(
            id=fake.random_number(),
            peer_id=PeerUser(fake.random_number()),
            date=fake.date(),
            message=f"PYTHON {fake.word()}",
        )
    )

    response = parser.parse_message(myself, sender, event)

    assert response is None


def test_parse_with_oi_message(parser, myself, sender):
    """
    Testando o metodo parse_message, com mensagem de oi.
    Nesse caso a mensagem deve passar e retornar os dados necessarios,
    Para responder a mensagem ao mesmo usuario que enviou.
    """

    event = NewMessage.Event(
        Message(
            id=fake.random_number(),
            peer_id=fake.random_number(),
            date=fake.date(),
            message="Oi",
        )
    )

    response = parser.parse_message(myself, sender, event)

    assert response["reply"] is True
    assert response["entity"] == sender.username
    assert response["message"] == "Oi, sou um bot de testes!"


def test_parse_with_noia_message(parser, myself, sender):
    """
    Testando o metodo parse_message, com mensagem de noia.
    Nesse caso a mensagem deve passar e retornar os dados necessarios,
    Para responder a mensagem ao mesmo usuario que enviou.
    """

    event = NewMessage.Event(
        Message(
            id=fake.random_number(),
            peer_id=fake.random_number(),
            date=fake.date(),
            message="Noia",
        )
    )

    response = parser.parse_message(myself, sender, event)

    assert response["reply"] is True
    assert response["entity"] == sender.username
    assert response["message"] == "Aloprado! (mensagem automatica)"


def test_parse_with_python_message_and_positive_filter(parser, myself, sender):
    """
    Testando o metodo parse_message, com python na mensagem e o filtro positivo.
    Recebendo uma mensagem com uma palavra do filtro.
    Nesse caso a mensagem deve passar e retornar os dados necessarios,
    Para o envio da mensagem ao grupo.
    """

    event = NewMessage.Event(
        Message(
            id=fake.random_number(),
            peer_id=fake.random_number(),
            date=fake.date(),
            message=f"Python : oportunidade {fake.word()}",
        )
    )

    response = parser.parse_message(myself, sender, event)

    assert response["forward"] is True
    assert response["entity"] == API["group"]
    assert response["message"] == event.message.message


def test_parse_with_python_message_and_negative_filter(parser, myself, sender):
    """
    Testando o metodo parse_message, com python na mensagem e o filtro negativo.
    Recebendo uma mensagem sem nenhuma das palavras do filtro.
    Nesse caso a mensagem nao deve passar e retornar None.
    """

    event = NewMessage.Event(
        Message(
            id=fake.random_number(),
            peer_id=fake.random_number(),
            date=fake.date(),
            message=f"Python {fake.word()}",
        )
    )

    response = parser.parse_message(myself, sender, event)

    assert response is None


def test_parse_without_any_by_the_filter_parameters(parser, myself, sender):
    """
    Testando o metodo parse_message, onde a mensagem nao contem nenhum dos parametros do filtro.
    O sistema deve retornar None.
    """

    event = NewMessage.Event(
        Message(
            id=fake.random_number(),
            peer_id=fake.random_number(),
            date=fake.date(),
            message=f"{fake.word()}",
        )
    )

    response = parser.parse_message(myself, sender, event)

    assert response is None


@mark.parametrize(
    "message",
    [
        ("Oportunidade de python saindo do forno guys!"),
        ("Tenho varias oportunidades para dev python rapaziada"),
        ("Tem vaga nova aqui na firma"),
        ("Tem muitas vagas novas aqui na firma"),
        ("Piazada, tem uma vaguinha de python muito boa aqui, se interessa?"),
        ("Vaguinhas fresquinhas aqui guys"),
        ("Quem estiver procurando emprego, eu estou com um de python aqui ein"),
        ("tem trabalho para programador python aqui"),
    ],
)
def test_words_filter_with_positive_filter(parser, message):
    """
    Testando o metodo words_filter.
    Realizao o teste com frases contendo todas as palavras do filtro para garantir que todas passam.
    Nesse caso deve retornar True.
    """

    response = parser.words_filter(message)

    assert response is True


@mark.parametrize(
    "message",
    [
        ("Bom dia piazada o python é uma linguagem muito boa"),
        ("estou estudando Python, que bom para mim"),
    ],
)
def test_words_filter_with_negative_filter(parser, message):
    """
    Testando o metodo words_filter.
    Realizao o teste com frases que nao contem nenhum palavra do filtro.
    Nesse caso deve retornar False.
    """

    response = parser.words_filter(message)

    assert response is False
