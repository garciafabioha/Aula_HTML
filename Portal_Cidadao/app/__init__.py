from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from config import Config

# Os objetos "db" e "mail" ficam aqui fora da função para poder ser
# importados por outros arquivos (ex: models.py, emails.py) sem criar
# dependência circular.
db = SQLAlchemy()
mail = Mail()

# LoginManager cuida da sessão de login do painel administrativo
# (Parte 5): sabe quem é o usuário logado em cada requisição e para
# onde mandar quem tentar acessar uma página protegida sem estar logado.
login_manager = LoginManager()
login_manager.login_view = "admin.login"
login_manager.login_message = "Faça login para acessar o painel administrativo."
login_manager.login_message_category = "aviso"


def create_app(config_class=Config):
    """Application factory.

    Em vez de criar o app Flask direto no módulo (app = Flask(__name__)),
    usamos uma função que cria e devolve o app. Isso é uma boa prática
    porque permite, por exemplo, criar múltiplas instâncias do app
    (uma para testes, outra para produção) com configurações diferentes.

    O parâmetro config_class é o que permite isso na prática: os testes
    (Parte 7) chamam create_app(TestConfig) para rodar com um banco
    SQLite em memória, isolado do banco de desenvolvimento/produção.
    """

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)

    # Importa os models para que o SQLAlchemy "conheça" as tabelas
    # antes de rodarmos db.create_all() (em init_db.py).
    from app import models  # noqa: F401
    from app.models import AdminUser

    @login_manager.user_loader
    def load_user(user_id):
        # Flask-Login guarda só o id (como string) na sessão e chama essa
        # função em toda requisição para recarregar o usuário completo.
        return db.session.get(AdminUser, int(user_id))

    # Registra as rotas (blueprints) da aplicação.
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    from app.admin_routes import admin_bp
    app.register_blueprint(admin_bp, url_prefix="/admin")

    # Filtro Jinja usado nos templates para colorir o status de um
    # protocolo com as cores de badge do Bootstrap (Parte 6):
    # {{ protocolo.status|badge_status }} -> "success", "danger", etc.
    from app.utils import status_badge_class
    app.jinja_env.filters["badge_status"] = status_badge_class

    return app
