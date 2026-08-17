from flask import Blueprint, flash, redirect, render_template, request, url_for

from app import db
from app.emails import enviar_email_protocolo
from app.forms import ProtocoloForm
from app.models import Protocolo
from app.utils import gerar_numero_protocolo

# Um Blueprint é um jeito de organizar rotas em grupos. Este (main_bp)
# tem só as rotas públicas, usadas pelo cidadão. Desde a Parte 5 existe
# também o admin_bp (app/admin_routes.py), com as rotas do painel
# administrativo, registrado à parte em app/__init__.py.
main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/protocolos/novo", methods=["GET", "POST"])
def novo_protocolo():
    form = ProtocoloForm()

    # validate_on_submit() só retorna True quando: (1) a requisição é POST
    # e (2) todos os validadores dos campos passaram. Se algo falhar,
    # form.errors é preenchido automaticamente e o template mostra as
    # mensagens de erro ao lado de cada campo.
    if form.validate_on_submit():
        numero = gerar_numero_protocolo()

        protocolo = Protocolo(
            numero=numero,
            nome_cidadao=form.nome_cidadao.data.strip(),
            email=form.email.data.strip() if form.email.data else None,
            tipo=form.tipo.data,
            descricao=form.descricao.data.strip(),
        )

        db.session.add(protocolo)
        db.session.commit()

        flash(
            f"Solicitação registrada com sucesso! Guarde seu número de protocolo: {numero}",
            "success",
        )

        if protocolo.email:
            enviado = enviar_email_protocolo(protocolo)
            if enviado:
                flash(f"Também enviamos esse número para {protocolo.email}.", "success")
            else:
                flash(
                    "Não foi possível enviar o e-mail de confirmação agora, "
                    "mas sua solicitação foi registrada normalmente.",
                    "aviso",
                )

        return redirect(url_for("main.protocolo_confirmacao", numero=numero))

    return render_template("novo_protocolo.html", form=form)


@main_bp.route("/protocolos/<numero>/confirmacao")
def protocolo_confirmacao(numero):
    protocolo = Protocolo.query.filter_by(numero=numero).first_or_404()
    return render_template("protocolo_confirmacao.html", protocolo=protocolo)


@main_bp.route("/protocolos/consultar")
def consultar_protocolo():
    # Usamos querystring (GET) em vez de POST aqui de propósito: assim o
    # cidadão pode salvar/compartilhar o link direto da consulta
    # (ex: http://.../protocolos/consultar?numero=PROT-2026-000001).
    numero = request.args.get("numero", "").strip().upper()

    protocolo = None
    buscou = bool(numero)

    if buscou:
        protocolo = Protocolo.query.filter_by(numero=numero).first()

    return render_template(
        "consultar_protocolo.html",
        numero=numero,
        protocolo=protocolo,
        buscou=buscou,
    )
