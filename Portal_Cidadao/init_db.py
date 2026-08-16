"""Cria as tabelas do banco de dados.

Rode este script uma vez (ou sempre que adicionar/alterar um model):

    python init_db.py
"""

from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()
    print("Tabelas criadas com sucesso.")
