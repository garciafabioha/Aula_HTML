from app.models import Protocolo


# --- Portão de login (before_request) ------------------------------------

def test_dashboard_sem_login_redireciona_para_login(client):
    r = client.get("/admin/", follow_redirects=False)
    assert r.status_code == 302
    assert "/admin/login" in r.headers["Location"]


def test_atualizar_status_sem_login_redireciona_para_login(client, protocolo):
    r = client.post(
        f"/admin/protocolos/{protocolo.id}/status",
        data={"status": "Concluído"},
        follow_redirects=False,
    )
    assert r.status_code == 302
    assert "/admin/login" in r.headers["Location"]


# --- Login / logout --------------------------------------------------------

def test_login_com_senha_errada_mostra_erro_e_nao_autentica(client, admin_user):
    r = client.post(
        "/admin/login",
        data={"username": "admin", "password": "senha-errada"},
        follow_redirects=True,
    )
    assert r.status_code == 200
    assert "Usuário ou senha inválidos".encode() in r.data

    # continua sem acesso ao painel
    r2 = client.get("/admin/", follow_redirects=False)
    assert r2.status_code == 302


def test_login_com_usuario_inexistente_mostra_erro(client):
    r = client.post(
        "/admin/login",
        data={"username": "nao-existe", "password": "qualquer"},
        follow_redirects=True,
    )
    assert "Usuário ou senha inválidos".encode() in r.data


def test_login_correto_permite_acessar_painel(logged_client):
    r = logged_client.get("/admin/")
    assert r.status_code == 200
    assert "Painel administrativo".encode() in r.data


def test_login_ja_autenticado_redireciona_direto_pro_painel(logged_client):
    r = logged_client.get("/admin/login", follow_redirects=False)
    assert r.status_code == 302
    assert r.headers["Location"].endswith("/admin/")


def test_logout_revoga_acesso(logged_client):
    logged_client.get("/admin/logout")
    r = logged_client.get("/admin/", follow_redirects=False)
    assert r.status_code == 302


def test_login_next_externo_e_ignorado_evita_open_redirect(client, admin_user):
    r = client.post(
        "/admin/login?next=https://site-malicioso.com/roubar-sessao",
        data={"username": "admin", "password": "senha123"},
        follow_redirects=False,
    )
    assert r.status_code == 302
    # precisa redirecionar para dentro do próprio site, nunca para fora
    assert r.headers["Location"].startswith("/") or "site-malicioso.com" not in r.headers["Location"]


# --- Listagem e filtro ------------------------------------------------------

def test_dashboard_lista_protocolos(logged_client, protocolo):
    r = logged_client.get("/admin/")
    assert protocolo.numero.encode() in r.data


def test_dashboard_filtro_por_status(logged_client, db):
    p_aberto = Protocolo(
        numero="PROT-2026-000001", nome_cidadao="A", tipo="Outros",
        descricao="Descrição com mais de dez caracteres.", status="Aberto",
    )
    p_concluido = Protocolo(
        numero="PROT-2026-000002", nome_cidadao="B", tipo="Outros",
        descricao="Descrição com mais de dez caracteres.", status="Concluído",
    )
    db.session.add_all([p_aberto, p_concluido])
    db.session.commit()

    r = logged_client.get("/admin/?status=Aberto")
    assert b"PROT-2026-000001" in r.data
    assert b"PROT-2026-000002" not in r.data


# --- Atualização de status ---------------------------------------------------

def test_atualizar_status_muda_status_no_banco(logged_client, protocolo, db):
    r = logged_client.post(
        f"/admin/protocolos/{protocolo.id}/status",
        data={"status": "Em andamento"},
        follow_redirects=True,
    )
    assert r.status_code == 200

    atualizado = db.session.get(Protocolo, protocolo.id)
    assert atualizado.status == "Em andamento"


def test_atualizar_status_valor_invalido_nao_altera_nada(logged_client, protocolo, db):
    logged_client.post(
        f"/admin/protocolos/{protocolo.id}/status",
        data={"status": "Status Inventado"},
        follow_redirects=True,
    )

    inalterado = db.session.get(Protocolo, protocolo.id)
    assert inalterado.status == "Aberto"


def test_atualizar_status_protocolo_inexistente_404(logged_client):
    r = logged_client.post("/admin/protocolos/99999/status", data={"status": "Aberto"})
    assert r.status_code == 404


def test_atualizar_status_preserva_filtro_no_redirecionamento(logged_client, protocolo):
    r = logged_client.post(
        f"/admin/protocolos/{protocolo.id}/status?status=Aberto",
        data={"status": "Em andamento"},
        follow_redirects=False,
    )
    assert r.status_code == 302
    assert "status=Aberto" in r.headers["Location"]
