import random
from datetime import datetime

from app.models import Protocolo

# Mapeia cada status para uma cor de badge do Bootstrap (Parte 6).
# Usado tanto no painel admin quanto nas páginas públicas de consulta,
# via o filtro Jinja "badge_status" registrado em app/__init__.py, para
# não duplicar essa lógica em cada template.
_STATUS_BADGE_CLASSES = {
    "Aberto": "secondary",
    "Em andamento": "info",
    "Concluído": "success",
    "Indeferido": "danger",
}


def status_badge_class(status):
    """Retorna a cor de badge do Bootstrap correspondente a um status.

    Usa "secondary" como padrão para qualquer status que não esteja no
    mapeamento acima (não deveria acontecer, já que o SelectField do
    painel admin só aceita os valores de STATUS_CHOICES, mas é melhor
    não quebrar a página caso apareça um valor inesperado).
    """

    return _STATUS_BADGE_CLASSES.get(status, "secondary")


def gerar_numero_protocolo():
    """Gera um número de protocolo único no formato PROT-AAAA-NNNNNN.

    Sorteia um sufixo de 6 dígitos e confere no banco se já não está em
    uso (a coluna "numero" tem uma restrição UNIQUE, então uma colisão
    aqui nunca resultaria em dado duplicado — mas é melhor evitar o erro
    checando antes).
    """

    ano = datetime.utcnow().year

    while True:
        sufixo = f"{random.randint(0, 999999):06d}"
        numero = f"PROT-{ano}-{sufixo}"

        ja_existe = Protocolo.query.filter_by(numero=numero).first()

        if not ja_existe:
            return numero
