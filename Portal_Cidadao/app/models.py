from datetime import datetime
from typing import Optional

from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import check_password_hash, generate_password_hash

from app import db

# Status possíveis de um protocolo, na ordem esperada do fluxo normal
# (Aberto -> Em andamento -> Concluído), mais "Indeferido" para quando a
# solicitação é negada. Centralizado aqui porque tanto o formulário do
# painel admin (app/admin_forms.py) quanto o valor padrão do model usam
# essa mesma lista.
STATUS_CHOICES = ["Aberto", "Em andamento", "Concluído", "Indeferido"]


class Protocolo(db.Model):
    """Representa uma solicitação/protocolo aberto por um cidadão.

    Cada linha nesta tabela é uma solicitação: um buraco na rua,
    um poste queimado, uma reclamação sobre algum serviço público, etc.

    Usa o estilo "declarativo tipado" do SQLAlchemy 2.0 (Mapped[...] +
    mapped_column(), em vez do antigo "coluna = db.Column(...)"). Na
    prática funciona exatamente igual — Protocolo(numero=..., ...)
    continua criando uma linha normalmente —, mas com essas anotações
    de tipo o SQLAlchemy consegue gerar um __init__ que o Pylance/
    Pyright entende, então ele para de reclamar de "parâmetro
    desconhecido" ao criar um Protocolo(...).
    """

    __tablename__ = "protocolos"

    id: Mapped[int] = mapped_column(primary_key=True)

    # Número público do protocolo, o que o cidadão usa para consultar
    # o status depois (ex: "PROT-2026-000123"). É diferente do "id"
    # interno do banco para não expor quantas linhas a tabela tem.
    numero: Mapped[str] = mapped_column(db.String(20), unique=True, nullable=False, index=True)

    nome_cidadao: Mapped[str] = mapped_column(db.String(120), nullable=False)
    email: Mapped[Optional[str]] = mapped_column(db.String(120), nullable=True)

    tipo: Mapped[str] = mapped_column(db.String(80), nullable=False)
    descricao: Mapped[str] = mapped_column(db.Text, nullable=False)

    # Aberto -> Em andamento -> Concluído (ou Indeferido)
    status: Mapped[str] = mapped_column(db.String(30), nullable=False, default="Aberto")

    data_abertura: Mapped[datetime] = mapped_column(db.DateTime, nullable=False, default=datetime.utcnow)
    data_atualizacao: Mapped[datetime] = mapped_column(
        db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def __repr__(self):
        return f"<Protocolo {self.numero} - {self.status}>"


class AdminUser(UserMixin, db.Model):
    """Usuário com acesso ao painel administrativo (Parte 5).

    Herda de UserMixin (Flask-Login) para ganhar de graça os métodos
    que a extensão precisa (is_authenticated, is_active, get_id, etc.).
    Não guardamos a senha em texto puro — só o hash, gerado com
    werkzeug.security (a mesma lib que o próprio Flask usa por baixo).

    Não existe cadastro pelo site: o primeiro (e demais) admins são
    criados rodando o script create_admin.py pelo terminal.
    """

    __tablename__ = "admin_users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(db.String(80), unique=True, nullable=False, index=True)
    password_hash: Mapped[str] = mapped_column(db.String(255), nullable=False)

    def set_password(self, senha):
        self.password_hash = generate_password_hash(senha)

    def check_password(self, senha):
        return check_password_hash(self.password_hash, senha)

    def __repr__(self):
        return f"<AdminUser {self.username}>"
