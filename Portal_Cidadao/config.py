import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Carrega variáveis do arquivo .env (se existir) para os.environ.
# Assim mantemos usuário/senha do banco fora do código-fonte.
load_dotenv(os.path.join(BASE_DIR, ".env"))


class Config:
    """Configurações da aplicação.

    Usamos uma classe de config para manter tudo centralizado.
    A string de conexão do banco vem da variável de ambiente
    DATABASE_URL (definida no arquivo .env), então trocar de
    banco no futuro não exige mexer em nenhum outro arquivo.
    """

    SECRET_KEY = os.environ.get("SECRET_KEY", "chave-de-desenvolvimento-trocar-depois")

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        f"sqlite:///{os.path.join(BASE_DIR, 'cidadao.db')}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
