from flask import Blueprint, render_template

# Um Blueprint é um jeito de organizar rotas em grupos.
# Por enquanto temos só um grupo (main_bp), mas na Parte 5
# (painel administrativo) provavelmente criaremos outro
# blueprint separado, ex: admin_bp.
main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("index.html")
