from urllib.parse import urlsplit

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user

from app import db
from app.admin_forms import LoginForm, StatusForm
from app.models import STATUS_CHOICES, AdminUser, Protocolo

# Blueprint separado do "main_bp" (rotas públicas), como já era previsto
# no comentário de routes.py desde a Parte 4. Fica registrado com
# url_prefix="/admin" em app/__init__.py, então toda rota daqui já
# nasce debaixo de /admin/... sem precisar repetir o prefixo abaixo.
admin_bp = Blueprint("admin", __name__)


@admin_bp.before_request
def exigir_login():
    """Portão único na frente de todo o painel administrativo.

    Em vez de colocar @login_required rota por rota (fácil de esquecer
    em alguma nova rota futura), este before_request roda antes de
    QUALQUER view deste blueprint e barra quem não está logado — a
    única exceção é a própria página de login, senão ninguém
    conseguiria nem chegar nela.
    """

    if request.endpoint == "admin.login":
        return None

    if not current_user.is_authenticated:
        # Guarda a URL que a pessoa queria acessar para, depois do
        # login, mandá-la de volta para lá em vez de sempre cair no
        # dashboard.
        return redirect(url_for("admin.login", next=request.full_path))

    return None


def _proxima_url_segura(candidata):
    """Só aceita redirecionar para caminhos internos do próprio site.

    Sem essa checagem, um link malicioso do tipo
    /admin/login?next=https://site-falso.com poderia usar nosso login
    para mandar o usuário, já autenticado, para fora do site
    (open redirect).
    """

    if not candidata:
        return None

    partes = urlsplit(candidata)
    if partes.netloc or partes.scheme:
        return None

    return candidata


@admin_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("admin.dashboard"))

    form = LoginForm()

    if form.validate_on_submit():
        # "or ''" antes do .strip() só para o verificador de tipos (o
        # WTForms tipa .data como "str | None"; o DataRequired() já
        # garante que não é None aqui, já que validate_on_submit() é True).
        usuario = AdminUser.query.filter_by(username=(form.username.data or "").strip()).first()

        if usuario and usuario.check_password(form.password.data):
            login_user(usuario)
            flash(f"Bem-vindo(a), {usuario.username}!", "success")

            destino = _proxima_url_segura(request.args.get("next"))
            return redirect(destino or url_for("admin.dashboard"))

        flash("Usuário ou senha inválidos.", "erro")

    return render_template("admin/login.html", form=form)


@admin_bp.route("/logout")
def logout():
    logout_user()
    flash("Você saiu do painel administrativo.", "success")
    return redirect(url_for("admin.login"))


@admin_bp.route("/")
def dashboard():
    status_filtro = request.args.get("status", "").strip()

    query = Protocolo.query.order_by(Protocolo.data_abertura.desc())
    if status_filtro:
        query = query.filter_by(status=status_filtro)

    protocolos = query.all()

    # Um StatusForm por protocolo (indexado pelo id) para que cada linha
    # da tabela tenha seu próprio select já pré-selecionado com o status
    # atual daquele protocolo.
    forms = {p.id: StatusForm(status=p.status) for p in protocolos}

    return render_template(
        "admin/dashboard.html",
        protocolos=protocolos,
        forms=forms,
        status_opcoes=STATUS_CHOICES,
        status_filtro=status_filtro,
    )


@admin_bp.route("/protocolos/<int:protocolo_id>/status", methods=["POST"])
def atualizar_status(protocolo_id):
    protocolo = db.get_or_404(Protocolo, protocolo_id)
    form = StatusForm()

    if form.validate_on_submit():
        status_antigo = protocolo.status
        protocolo.status = form.status.data
        db.session.commit()

        if status_antigo != protocolo.status:
            flash(
                f'Status do protocolo {protocolo.numero} atualizado para "{protocolo.status}".',
                "success",
            )
        else:
            flash(f"Status do protocolo {protocolo.numero} não foi alterado.", "aviso")
    else:
        flash("Não foi possível atualizar o status. Tente novamente.", "erro")

    # Preserva o filtro de status que estava aplicado na listagem
    # (veio como querystring na própria action do formulário).
    status_filtro = request.args.get("status", "")
    return redirect(url_for("admin.dashboard", status=status_filtro))
