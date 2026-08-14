# Importar as bibliotecas
import time
import sqlite3
import numpy as np
import pandas as pd
import streamlit as st

# Config.iniciais da página
st.set_page_config(
    page_title='Performace e Caching Pro',
    page_icon='⚡', 
    layout='wide'
)

# Titulo da página
st.title('Aula 03: Estratégias de Caching: Data vs Resource')

# Demonstração de st.cache_data
@st.cache_data(show_spinner='Processando Base de Dados...')
def carregar_transformar_dados(linhas=50_000):
    """
    Simula uma operação de carga e limpeza de dados pesados:
    Utilizamos st.cache_data porque o retorno é um objeto sereializável (DataFrame).
    """
    # Simular a latência de processamento ou E/S
    time.sleep(3)

    # Criar os dados
    dados = pd.DataFrame(
        np.random.randn(linhas, 4),
        columns=['col_1', 'col_2', 'col_3', 'col_4']
    )

    # Simular a transformação de dados
    dados = dados.apply(lambda x: x * 100)

    return dados

st.header('Otimização de Dados com st.cache_data')

# Interface para disparar a carga de dados
linhas = st.slider(
    label='Quantidade de linhas para processar',
    min_value=5_000,
    max_value=100_000,
    step=5_000,
    value=50_000
)

t_i = time.time()
df = carregar_transformar_dados(linhas)
t_f = time.time()

st.success(f'Operação concluída em {t_f - t_i:.2f} segundos!')
st.dataframe(df)

st.divider()

# Gerenciamento de memória e expiração
st.header('Controle de Expiração e Limites de Memória')

@st.cache_data(ttl='10s', max_entries=20)
def obter_metricas_api(categoria):
    """
    Simula a busca de métricas em uma API externa que muda periodicamente
    O parâmetro ttl(Time-To-Live) garante que os dados não fiquem absoletos.
    O parâmetro max_entries evita o estou de memória (DOM).
    """
    st.toast(f'Consultando API para categoria: {categoria}')
    time.sleep(1.5)

    metricas = {
        'categoria': categoria,
        'timestemp': time.ctime(),
        'valor': np.random.uniform(100, 1000)
    }

    return metricas

# Seleção de categoris para testar o cache com TTL
api_cat = st.radio(
    label='Selecione a categoria da metrica',
    options=['Visitas', 'Vendas', 'Devoluções'],
    horizontal=True
)

if st.button('Buscar métricas'):
    metricas = obter_metricas_api(api_cat)
    st.write('Dados recuperados da API (ou cache):')
    st.json(metricas)
    st.info('Este dado será mantido em cache por no máximo 10 segundos (TTL)')

st.divider()

st.header('Persistência de Recursos com st.cache_resource')

@st.cache_resource
def obter_engine_banco_dados():
    """
    Inicializa um motor de conexão SQL.
    Usamos st.cache_resource pois a conexão não é serializável.
    Este objeto serás compartilhado entre todos os usuários da aplicação.
    """
    st.warning('⚙️ Inicializando o Motor do Banco de Dados (Recurso Global)...')

    # Simulaçào de inicialização de um recurso pesado (banco de dados ou modelo de ML)
    time.sleep(2)

    # Criar uma conexão SQLite em memória
    conn = sqlite3.connect(':memory:', check_same_thread=True)

    return conn

# Inicializar o recurso
bd_engine = obter_engine_banco_dados()

st.write('O motor de banco de dados está pronto e em memória.')
st.caption('Recurso cacheados via st.cache_resource agem com Singletons e não são copiados.')

