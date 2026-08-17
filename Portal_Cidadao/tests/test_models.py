from app.models import STATUS_CHOICES, AdminUser, Protocolo


def test_protocolo_status_padrao_e_aberto(db):
    p = Protocolo(
        numero="PROT-2026-000099",
        nome_cidadao="Teste",
        tipo="Outros",
        descricao="Descrição qualquer com mais de dez caracteres.",
    )
    db.session.add(p)
    db.session.commit()

    assert p.status == "Aberto"
    assert p.data_abertura is not None
    assert p.data_atualizacao is not None


def test_protocolo_numero_precisa_ser_unico(db):
    dados = dict(
        numero="PROT-2026-000001",
        nome_cidadao="Fulano",
        tipo="Outros",
        descricao="Descrição qualquer com mais de dez caracteres.",
    )
    db.session.add(Protocolo(**dados))
    db.session.commit()

    db.session.add(Protocolo(**dados))
    try:
        db.session.commit()
        assert False, "deveria ter levantado um erro de UNIQUE constraint"
    except Exception:
        db.session.rollback()


def test_status_choices_tem_os_quatro_status_esperados():
    assert STATUS_CHOICES == ["Aberto", "Em andamento", "Concluído", "Indeferido"]


def test_admin_user_nao_guarda_senha_em_texto_puro(db):
    admin = AdminUser(username="admin")
    admin.set_password("minha-senha-123")
    db.session.add(admin)
    db.session.commit()

    assert admin.password_hash != "minha-senha-123"
    assert admin.check_password("minha-senha-123") is True
    assert admin.check_password("senha-errada") is False


def test_admin_user_username_precisa_ser_unico(db):
    a1 = AdminUser(username="admin")
    a1.set_password("senha123")
    db.session.add(a1)
    db.session.commit()

    a2 = AdminUser(username="admin")
    a2.set_password("outrasenha")
    db.session.add(a2)
    try:
        db.session.commit()
        assert False, "deveria ter levantado um erro de UNIQUE constraint"
    except Exception:
        db.session.rollback()
