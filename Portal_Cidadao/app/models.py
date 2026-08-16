from datetime import datetime

from app import db


class Protocolo(db.Model):
    """Representa uma solicitação/protocolo aberto por um cidadão.

    Cada linha nesta tabela é uma solicitação: um buraco na rua,
    um poste queimado, uma reclamação sobre algum serviço público, etc.
    """

    __tablename__ = "protocolos"

    id = db.Column(db.Integer, primary_key=True)

    # Número público do protocolo, o que o cidadão usa para consultar
    # o status depois (ex: "PROT-2026-000123"). É diferente do "id"
    # interno do banco para não expor quantas linhas a tabela tem.
    numero = db.Column(db.String(20), unique=True, nullable=False, index=True)

    nome_cidadao = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=True)

    tipo = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.Text, nullable=False)

    # Aberto -> Em andamento -> Concluído (ou Indeferido)
    status = db.Column(db.String(30), nullable=False, default="Aberto")

    data_abertura = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    data_atualizacao = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def __repr__(self):
        return f"<Protocolo {self.numero} - {self.status}>"
