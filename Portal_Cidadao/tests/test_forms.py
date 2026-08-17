from app.admin_forms import LoginForm, StatusForm
from app.forms import ProtocoloForm


def test_protocolo_form_dados_validos_passam(app):
    with app.test_request_context(
        method="POST",
        data={
            "nome_cidadao": "Maria Teste",
            "email": "maria@example.com",
            "tipo": "Buraco na via",
            "descricao": "Descrição com mais de dez caracteres.",
        },
    ):
        form = ProtocoloForm()
        assert form.validate() is True


def test_protocolo_form_nome_obrigatorio(app):
    with app.test_request_context(
        method="POST",
        data={
            "nome_cidadao": "",
            "tipo": "Outros",
            "descricao": "Descrição com mais de dez caracteres.",
        },
    ):
        form = ProtocoloForm()
        assert form.validate() is False
        assert "nome_cidadao" in form.errors


def test_protocolo_form_email_invalido_e_rejeitado(app):
    with app.test_request_context(
        method="POST",
        data={
            "nome_cidadao": "Maria",
            "email": "isso-nao-e-um-email",
            "tipo": "Outros",
            "descricao": "Descrição com mais de dez caracteres.",
        },
    ):
        form = ProtocoloForm()
        assert form.validate() is False
        assert "email" in form.errors


def test_protocolo_form_email_vazio_e_opcional(app):
    with app.test_request_context(
        method="POST",
        data={
            "nome_cidadao": "Maria",
            "email": "",
            "tipo": "Outros",
            "descricao": "Descrição com mais de dez caracteres.",
        },
    ):
        form = ProtocoloForm()
        assert form.validate() is True


def test_protocolo_form_descricao_curta_e_rejeitada(app):
    with app.test_request_context(
        method="POST",
        data={
            "nome_cidadao": "Maria",
            "tipo": "Outros",
            "descricao": "curta",
        },
    ):
        form = ProtocoloForm()
        assert form.validate() is False
        assert "descricao" in form.errors


def test_login_form_exige_usuario_e_senha(app):
    with app.test_request_context(method="POST", data={"username": "", "password": ""}):
        form = LoginForm()
        assert form.validate() is False
        assert "username" in form.errors
        assert "password" in form.errors


def test_status_form_aceita_valor_da_lista(app):
    with app.test_request_context(method="POST", data={"status": "Em andamento"}):
        form = StatusForm()
        assert form.validate() is True


def test_status_form_rejeita_valor_fora_da_lista(app):
    with app.test_request_context(method="POST", data={"status": "Status Inventado"}):
        form = StatusForm()
        assert form.validate() is False
        assert "status" in form.errors
