import re
from datetime import datetime

from app.models import STATUS_CHOICES
from app.utils import gerar_numero_protocolo, status_badge_class


def test_gerar_numero_protocolo_segue_o_formato_esperado(app):
    with app.app_context():
        numero = gerar_numero_protocolo()

    ano_atual = datetime.utcnow().year
    assert re.fullmatch(rf"PROT-{ano_atual}-\d{{6}}", numero)


def test_gerar_numero_protocolo_nao_repete_numero_existente(app, db):
    from app.models import Protocolo

    with app.app_context():
        # Fixa o "aleatório" gerando um número, garantindo que já existe
        # no banco, e confere que uma segunda chamada não devolve o
        # mesmo valor.
        numero_existente = gerar_numero_protocolo()
        db.session.add(
            Protocolo(
                numero=numero_existente,
                nome_cidadao="Teste",
                tipo="Outros",
                descricao="Descrição qualquer com mais de dez caracteres.",
            )
        )
        db.session.commit()

        outro_numero = gerar_numero_protocolo()
        assert outro_numero != numero_existente


def test_status_badge_class_cobre_todos_os_status_conhecidos():
    esperado = {
        "Aberto": "secondary",
        "Em andamento": "info",
        "Concluído": "success",
        "Indeferido": "danger",
    }

    for status in STATUS_CHOICES:
        assert status_badge_class(status) == esperado[status]


def test_status_badge_class_usa_secondary_como_padrao_para_status_desconhecido():
    assert status_badge_class("Status Que Não Existe") == "secondary"
