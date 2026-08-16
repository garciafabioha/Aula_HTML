from flask import current_app
from flask_mail import Message

from app import mail


def enviar_email_protocolo(protocolo):
    """Envia um e-mail ao cidadão com o número do protocolo criado.

    Retorna True se o e-mail foi enviado, False se não foi (seja porque
    o servidor de e-mail não está configurado, seja por algum erro no
    envio). O chamador decide o que fazer com esse retorno — não
    levantamos exceção aqui porque falha no envio de e-mail não deve
    impedir o cidadão de ver a confirmação do protocolo na tela.
    """

    if not protocolo.email:
        return False

    # Se MAIL_USERNAME não estiver configurado no .env, nem tentamos
    # enviar — evita um erro de conexão toda vez que alguém testar o
    # formulário sem ter configurado e-mail ainda.
    if not current_app.config.get("MAIL_USERNAME"):
        current_app.logger.warning(
            "Envio de e-mail não configurado (MAIL_USERNAME ausente); "
            "e-mail de confirmação do protocolo %s não foi enviado.",
            protocolo.numero,
        )
        return False

    corpo = f"""Olá, {protocolo.nome_cidadao},

Sua solicitação foi registrada com sucesso no Portal do Cidadão.

Número do protocolo: {protocolo.numero}
Tipo: {protocolo.tipo}
Status atual: {protocolo.status}

Guarde este número para consultar o andamento da sua solicitação
quando quiser.

Portal do Cidadão
"""

    mensagem = Message(
        subject=f"Protocolo {protocolo.numero} registrado com sucesso",
        recipients=[protocolo.email],
        body=corpo,
    )

    try:
        mail.send(mensagem)
        return True
    except Exception:
        # Loga o erro completo nos logs do servidor, mas não deixa a
        # aplicação quebrar por causa disso.
        current_app.logger.exception(
            "Falha ao enviar e-mail de confirmação do protocolo %s",
            protocolo.numero,
        )
        return False
