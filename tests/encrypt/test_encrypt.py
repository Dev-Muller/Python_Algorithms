from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("teste", "teste")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 1)

    assert encrypt_message("teste", 10) == "etset"
    assert encrypt_message("teste", 1) == "t_etse"
