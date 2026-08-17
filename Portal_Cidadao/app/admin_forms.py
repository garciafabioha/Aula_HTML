from flask_wtf import FlaskForm
from wtforms import PasswordField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length

from app.models import STATUS_CHOICES


class LoginForm(FlaskForm):
    """Formulário de login do painel administrativo."""

    username = StringField(
        "Usuário",
        validators=[DataRequired(message="Informe o usuário.")],
    )

    password = PasswordField(
        "Senha",
        validators=[DataRequired(message="Informe a senha.")],
    )

    submit = SubmitField("Entrar")


class StatusForm(FlaskForm):
    """Formulário (um por protocolo) usado para trocar o status na
    listagem do painel admin.

    As choices vêm da mesma lista STATUS_CHOICES usada no model, então
    o WTForms recusa automaticamente qualquer valor enviado que não
    esteja nessa lista (proteção contra alguém adulterar o POST e
    mandar um status inventado).
    """

    status = SelectField(
        "Status",
        choices=[(s, s) for s in STATUS_CHOICES],
        validators=[
            DataRequired(message="Selecione um status."),
            Length(max=30),
        ],
    )

    submit = SubmitField("Atualizar")
