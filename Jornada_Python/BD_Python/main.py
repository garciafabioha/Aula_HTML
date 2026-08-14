import time
import streamlit as st
from script_db import criar_tabela, insert_usuario, select_usuarios, update_usuarios, delete_usuarios

criar_tabela()

# ===== CADASTRO =====
st.title("Cadastro de Usuário")

if "limpar" not in st.session_state:
    st.session_state.limpar = False

if st.session_state.limpar:
    st.session_state.limpar = False
    st.session_state.nome = ""

with st.form("form_cadastro"):
    nome = st.text_input("Nome do Usuário", key="nome")
    tipo = st.selectbox("Tipo do usuário", ["Administrador", "Convidado", "Moderador", "Usuário Comum"])
    enviar = st.form_submit_button("Cadastrar")

if enviar:
    if nome.strip():
        insert_usuario(nome.strip(), tipo)
        mensagem = st.empty()
        mensagem.success(f"Usuário **{nome}** cadastrado com sucesso!")
        time.sleep(3)
        mensagem.empty()
        st.session_state.limpar = True
        st.rerun()
    else:
        st.error("O nome do usuário é obrigatório!")

# ===== PESQUISA =====
st.divider()
st.subheader("Pesquisar Usuários")

if "limpar_busca" not in st.session_state:
    st.session_state.limpar_busca = False

if "pesquisou" not in st.session_state:
    st.session_state.pesquisou = False

# flag para controlar exibição do formulário de edição
if "editando_id" not in st.session_state:
    st.session_state.editando_id = None

if "acao" not in st.session_state:
    st.session_state.acao = None    

if st.session_state.limpar_busca:
    st.session_state.limpar_busca = False
    st.session_state.pesquisou = False
    st.session_state.editando_id = None
    st.session_state.acao = None
    st.session_state.pop("resultado_busca", None)
    if "busca_temp" in st.session_state:
        del st.session_state["busca_temp"]

nome_busca = st.text_input(
    "Digite o nome para pesquisar (deixe vazio para listar todos)",
    key="busca_temp"
)

col1, col2, col3, col4 = st.columns([2, 2, 2, 2])
#Botões das ações
with col1:
    pesquisar = st.button("Pesquisar")
with col2:
    limpar_pesquisa = st.button("Limpar a Pesquisa")
with col3:
    alterar_nome = st.button("Alterar Nome")
with col4:
    apagar_usuario = st.button("Apagar Cadastro")

if limpar_pesquisa:
    st.session_state.limpar_busca = True
    st.rerun()

if pesquisar:
    st.session_state.pesquisou = True
    st.session_state.editando_id = None  # fecha edição aberta ao pesquisar novamente
    st.session_state["resultado_busca"] = select_usuarios(nome_busca.strip())

if alterar_nome:
    if st.session_state.pesquisou and "resultado_busca" in st.session_state:
        usuarios = st.session_state["resultado_busca"]
        if usuarios:
            st.session_state.editando_id = usuarios[0].id
            st.session_state.acao = "editar"        # ← faltava isso
    else:
        st.warning("Pesquise um usuário antes de alterar!")

if apagar_usuario:
    if st.session_state.pesquisou and "resultado_busca" in st.session_state:
        usuarios = st.session_state["resultado_busca"]
        if usuarios:
            st.session_state.editando_id = usuarios[0].id
            st.session_state.acao = "deletar"
    else:
        st.warning("Pesquise um usuário antes de apagar!")

# exibe resultado da pesquisa
if st.session_state.pesquisou and "resultado_busca" in st.session_state:
    usuarios = st.session_state["resultado_busca"]
    if usuarios:
        for u in usuarios:
            st.write(f"**{u.nome}** — {u.tipo} — ID: {u.id}")

    # exibe formulário de edição somente para o usuário selecionado
        if st.session_state.editando_id == u.id:
            if st.session_state.acao == "deletar":
                st.warning(f"Tem certeza que deseja apagar **{u.nome}**?")
                col_sim, col_nao = st.columns([1, 5])
                with col_sim:
                    if st.button("Sim, apagar", key=f"confirmar_{u.id}"):
                        delete_usuarios(u.id)
                        st.success(f"Usuário **{u.nome}** apagado com sucesso!")
                        st.session_state.editando_id = None
                        st.session_state.acao = None
                        busca_atual = st.session_state.get("busca_temp", "")
                        st.session_state["resultado_busca"] = select_usuarios(busca_atual.strip())
                        time.sleep(1)
                        st.rerun()
                with col_nao:
                    if st.button("Cancelar", key=f"cancelar_del_{u.id}"):
                        st.session_state.editando_id = None
                        st.session_state.acao = None
                        st.rerun()

            elif st.session_state.acao == "editar":
                with st.form(f"form_editar_{u.id}"):
                    novo_nome = st.text_input("Novo nome", value=u.nome)
                    col_salvar, col_cancelar = st.columns([2, 2])
                    with col_salvar:
                        salvar = st.form_submit_button("Salvar")
                    with col_cancelar:
                        cancelar = st.form_submit_button("Cancelar")

                if salvar:
                    if novo_nome.strip():
                        update_usuarios(u.id, novo_nome.strip())
                        st.success(f"Nome atualizado para **{novo_nome.strip()}** com sucesso!")
                        st.session_state.editando_id = None
                        st.session_state.acao = None
                        busca_atual = st.session_state.get("busca_temp", "")
                        st.session_state["resultado_busca"] = select_usuarios(busca_atual.strip())
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error("O novo nome não pode ser vazio!")

                if cancelar:
                    st.session_state.editando_id = None
                    st.session_state.acao = None
                    st.rerun()


            st.divider()
    else:
        st.warning("Nenhum usuário encontrado!")
