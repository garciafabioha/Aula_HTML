"""Fixtures compartilhadas por toda a suíte de testes (Parte 7).

Cada teste roda contra um banco SQLite em memória, criado do zero e
descartado no final — nunca tocamos no banco real de desenvolvimento.
"""

import pytest

from app import create_app
from app import db as _db
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SECRET_KEY = "chave-de-teste"
    # Desligamos o CSRF na maioria dos testes para simplificar os POSTs
    # (o comportamento do CSRF em si é validado à parte, em
    # test_csrf.py, com um app que o mantém ligado).
    WTF_CSRF_ENABLED = False
    MAIL_USERNAME = None


@pytest.fixture()
def app():
    application = create_app(TestConfig)

    with application.app_context():
        _db.create_all()
        yield application
        _db.session.remove()
        _db.drop_all()


@pytest.fixture()
def db(app):
    return _db


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def admin_user(db):
    from app.models import AdminUser

    admin = AdminUser(username="admin")
    admin.set_password("senha123")
    db.session.add(admin)
    db.session.commit()
    return admin


@pytest.fixture()
def protocolo(db):
    from app.models import Protocolo

    p = Protocolo(
        numero="PROT-2026-000001",
        nome_cidadao="Maria Teste",
        email="maria@example.com",
        tipo="Buraco na via",
        descricao="Buraco grande na rua principal, atrapalha o trânsito.",
        status="Aberto",
    )
    db.session.add(p)
    db.session.commit()
    return p


@pytest.fixture()
def logged_client(client, admin_user):
    """Cliente de teste já autenticado como admin."""

    client.post(
        "/admin/login",
        data={"username": admin_user.username, "password": "senha123"},
        follow_redirects=True,
    )
    return client
