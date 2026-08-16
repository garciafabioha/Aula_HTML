from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

# O objeto "db" fica aqui fora da função para poder ser
# importado por outros arquivos (ex: models.py) sem criar
# dependência circular.
db = SQLAlchemy()


def create_app():
    """Application factory.

    Em vez de criar o app Flask direto no módulo (app = Flask(__name__)),
    usamos uma função que cria e devolve o app. Isso é uma boa prática
    porque permite, por exemplo, criar múltiplas instâncias do app
    (uma para testes, outra para produção) com configurações diferentes.
    """

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Importa os models para que o SQLAlchemy "conheça" as tabelas
    # antes de rodarmos db.create_all() (em init_db.py).
    from app import models  # noqa: F401

    # Registra as rotas (blueprint) da aplicação.
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
