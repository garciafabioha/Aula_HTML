import random
from datetime import datetime

from app.models import Protocolo


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
