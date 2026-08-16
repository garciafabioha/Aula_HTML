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

    # Configuração de envio de e-mail (usada para mandar o número do
    # protocolo ao cidadão). Se MAIL_USERNAME não estiver definido no
    # .env, o sistema simplesmente não tenta enviar e-mails — não é
    # obrigatório configurar isso para o resto do projeto funcionar.
    MAIL_SERVER = os.environ.get("MAIL_SERVER", "smtp.gmail.com")
    MAIL_PORT = int(os.environ.get("MAIL_PORT", 587))
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS", "true").lower() == "true"
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER", MAIL_USERNAME)
