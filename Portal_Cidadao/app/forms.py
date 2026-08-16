from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, Optional

# Tipos de solicitação disponíveis. Centralizar essa lista aqui facilita
# adicionar novos tipos no futuro sem precisar mexer nas rotas/templates.
TIPOS_SOLICITACAO = [
    "Iluminação pública",
    "Buraco na via",
    "Coleta de lixo",
    "Poda de árvore",
    "Saneamento/esgoto",
    "Outros",
]


class ProtocoloForm(FlaskForm):
    """Formulário de abertura de um novo protocolo/solicitação.

    O Flask-WTF cuida de duas coisas importantes por baixo dos panos:
    1. Proteção CSRF (evita que outro site envie um formulário falso
       em nome do usuário sem ele saber).
    2. Validação dos campos antes de tocarmos no banco de dados.
    """

    nome_cidadao = StringField(
        "Nome completo",
        validators=[
            DataRequired(message="Informe seu nome."),
            Length(max=120, message="Nome muito longo (máximo 120 caracteres)."),
        ],
    )

    email = StringField(
        "E-mail (opcional)",
        validators=[
            Optional(),
            Email(message="Informe um e-mail válido."),
            Length(max=120),
        ],
    )

    tipo = SelectField(
        "Tipo de solicitação",
        choices=[(t, t) for t in TIPOS_SOLICITACAO],
        validators=[DataRequired(message="Selecione o tipo de solicitação.")],
    )

    descricao = TextAreaField(
        "Descrição da solicitação",
        validators=[
            DataRequired(message="Descreva sua solicitação."),
            Length(
                min=10,
                max=2000,
                message="A descrição deve ter entre 10 e 2000 caracteres.",
            ),
        ],
    )

    submit = SubmitField("Enviar solicitação")
