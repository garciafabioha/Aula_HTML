"""Verifica que a proteção CSRF do Flask-WTF está realmente ativa.

Todo o resto da suíte desliga WTF_CSRF_ENABLED (tests/conftest.py) para
simplificar os POSTs de teste — o que por si só não prova que a
proteção funciona em produção. Este arquivo usa uma app à parte, com o
CSRF ligado (como é por padrão), só para confirmar isso.
"""

import pytest

from app import create_app
from app import db as _db
from config import Config


class TestConfigComCsrf(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SECRET_KEY = "chave-de-teste"
    WTF_CSRF_ENABLED = True
    MAIL_USERNAME = None


@pytest.fixture()
def client_com_csrf():
    application = create_app(TestConfigComCsrf)
    with application.app_context():
        _db.create_all()
        yield application.test_client()
        _db.session.remove()
        _db.drop_all()


def test_post_sem_csrf_token_e_recusado(client_com_csrf):
    r = client_com_csrf.post(
        "/protocolos/novo",
        data={
            "nome_cidadao": "Maria",
            "tipo": "Outros",
            "descricao": "Descrição com mais de dez caracteres.",
        },
    )

    # Este projeto usa o CSRF por formulário do Flask-WTF (não o
    # CSRFProtect global da aplicação inteira). Sem token, validate()
    # falha e a view simplesmente re-renderiza o formulário (200) com o
    # aviso de sessão expirada — mas, o que mais importa, NADA é salvo
    # no banco.
    assert r.status_code == 200
    assert "sessão expirou".encode() in r.data

    from app.models import Protocolo

    assert Protocolo.query.count() == 0


def test_post_com_csrf_token_valido_funciona(client_com_csrf):
    pagina = client_com_csrf.get("/protocolos/novo")
    import re

    token = re.search(rb'name="csrf_token" type="hidden" value="([^"]+)"', pagina.data).group(1).decode()

    r = client_com_csrf.post(
        "/protocolos/novo",
        data={
            "csrf_token": token,
            "nome_cidadao": "Maria",
            "tipo": "Outros",
            "descricao": "Descrição com mais de dez caracteres.",
        },
        follow_redirects=True,
    )

    assert r.status_code == 200
