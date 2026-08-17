from app.models import Protocolo


def test_index_carrega(client):
    r = client.get("/")
    assert r.status_code == 200
    assert "Portal do Cidadão".encode() in r.data


def test_novo_protocolo_get_mostra_formulario(client):
    r = client.get("/protocolos/novo")
    assert r.status_code == 200
    assert b"nome_cidadao" in r.data


def test_novo_protocolo_post_valido_cria_registro_e_redireciona(client, db):
    r = client.post(
        "/protocolos/novo",
        data={
            "nome_cidadao": "João da Silva",
            "email": "",
            "tipo": "Poda de árvore",
            "descricao": "Árvore com galhos quebrados sobre a calçada.",
        },
        follow_redirects=True,
    )

    assert r.status_code == 200
    protocolos = Protocolo.query.all()
    assert len(protocolos) == 1
    assert protocolos[0].nome_cidadao == "João da Silva"
    assert protocolos[0].numero.encode() in r.data


def test_novo_protocolo_post_invalido_nao_cria_registro(client, db):
    r = client.post(
        "/protocolos/novo",
        data={
            "nome_cidadao": "",
            "tipo": "Outros",
            "descricao": "curta",
        },
    )

    assert r.status_code == 200  # re-renderiza o form, não redireciona
    assert Protocolo.query.count() == 0


def test_consultar_protocolo_existente_mostra_detalhes(client, protocolo):
    r = client.get(f"/protocolos/consultar?numero={protocolo.numero}")
    assert r.status_code == 200
    assert protocolo.numero.encode() in r.data
    assert protocolo.nome_cidadao.encode() in r.data


def test_consultar_protocolo_inexistente_mostra_mensagem(client):
    r = client.get("/protocolos/consultar?numero=PROT-2026-999999")
    assert r.status_code == 200
    assert "Nenhuma solicitação encontrada".encode() in r.data


def test_consultar_protocolo_sem_numero_nao_busca(client):
    r = client.get("/protocolos/consultar")
    assert r.status_code == 200
    assert "Nenhuma solicitação encontrada".encode() not in r.data


def test_protocolo_confirmacao_existente(client, protocolo):
    r = client.get(f"/protocolos/{protocolo.numero}/confirmacao")
    assert r.status_code == 200
    assert protocolo.numero.encode() in r.data


def test_protocolo_confirmacao_inexistente_404(client):
    r = client.get("/protocolos/PROT-2026-999999/confirmacao")
    assert r.status_code == 404
