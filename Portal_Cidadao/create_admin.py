"""Cria um usuário administrador para acessar o painel em /admin.

Não existe cadastro pelo site de propósito (o painel é só para a
prefeitura/equipe interna) — rode este script pelo terminal sempre que
precisar criar um novo admin:

    python create_admin.py
"""

import getpass

from app import create_app, db
from app.models import AdminUser

app = create_app()

with app.app_context():
    username = input("Usuário do admin: ").strip()

    if not username:
        print("Usuário não pode ser vazio. Nada foi criado.")
        raise SystemExit(1)

    if AdminUser.query.filter_by(username=username).first():
        print(f'Já existe um admin com o usuário "{username}".')
        raise SystemExit(1)

    senha = getpass.getpass("Senha: ")
    confirmacao = getpass.getpass("Confirme a senha: ")

    if len(senha) < 6:
        print("A senha deve ter pelo menos 6 caracteres. Nada foi criado.")
        raise SystemExit(1)

    if senha != confirmacao:
        print("As senhas não coincidem. Nada foi criado.")
        raise SystemExit(1)

    admin = AdminUser(username=username)
    admin.set_password(senha)

    db.session.add(admin)
    db.session.commit()

    print(f'Admin "{username}" criado com sucesso. Já pode fazer login em /admin/login.')
