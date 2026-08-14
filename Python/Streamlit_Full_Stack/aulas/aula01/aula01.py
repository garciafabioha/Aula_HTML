# Bibliotecas 
import datetime
import streamlit as st

# Configuração layout da página
st.set_page_config(layout='wide')

# Inicialização
st.title('Sistema de Gestão de Missões e Dados 🚀') 
st.header('Módulo de Controle e Entrega de Parâmetros')
st.subheader('Configuração de Variáveis de Operação')
st.write('Este ambiente de controle utiliza a arquitetura de reexecução linear do Streamlit.',
         'Cada interaçao com os widgets abaixo desencadeia uma atualização do estado global,',
         ' garantindo que a visualização reflita os dados em tempo real.')

# Linha de divisão
st.divider()

# Entrada de texto
nome_operacao = st.text_input(
    label='Nome da operação:',
    placeholder='Digite o codinome da missão...',
    key='entrada_nome_operacao',
    help='Este nome será usado para gerar os relatórios automáticos.'
)

# Entrada numérica com validação de limites
capacidade_equipe = st.number_input(
    label='Capacidade total da equipe (membros)',
    min_value=1,
    max_value=50,
    value=5,
    step=1,
    key='entrada_capacidade_equipe'
)

# Escrever a saída
st.write(f'Operação **{nome_operacao}** configurada para <b>{capacidade_equipe}</b> integrantes.',
         unsafe_allow_html=True)

# Adicionar seleções tradicionar aprimoradas
# Linha de divisão
st.divider()
# Uma nova sub seção do header
st.subheader('Parâmetros de Comunicação e Prioridade')

# st.radio() com captions (legendas)
canal_comunicacao = st.radio(
    label='Canal de comunicação preferêncial:',
    options=['**Base Aérea**', '**Quartel**', '**Base Médica**', '**Torpedeiro**'],
    captions=['*Brig. Dantas*', '*Gen. Afonso*', '*Dr. Clóvis*', '*Alm. Peixoto*'],
    index = 0,
    horizontal=True,
    key='radio_comunicacao'
) 

# Casa de seleção st.selectbox() com placeholder e entrada de novas opções
prioridade_missao = st.selectbox(
    label='Nível de prioridade da missão',
    options=['Baixa', 'Média', 'Alta'],
    index=None,
    placeholder='Selecione a prioridade...',
    accept_new_options=True,
    key='selecao_prioridade'
)

# Saída
st.write(f'Canal:**{canal_comunicacao}** | Prioridade: **{prioridade_missao}**')

# Seleção moderna utilizando st.pills() e st.segmented_control()
# Linha de divisão
st.divider()
# Uma nova sub seção do header
st.subheader('Configurações Avançadas de Seleção')

# Uso de st.pills() para seleção de status
status_missao = st.pills(
    label='Status atual do projeto',
    options=['Planejamento', 'Execução', 'Concluído', 'Arquivado'],
    selection_mode='single',
    default='Planejamento',
    key='pills.status'
)

# Uso st.segmented_control() para multiplos filtros
setores_afetados = st.segmented_control(
    label='Setores de impacto direto',
    options=['Administrativo', 'Arsenal', 'Suprimentos', 'Logística'],
    selection_mode='multi',
    default='Logística',
    width='stretch',
    key='segmented_setores'
)

# Escrever a saída
st.write(f'A missão está em fase de **{status_missao}** impactando: **{", ".join(setores_afetados)}**')

# Controle de cronograma com widgets temporais
# Linha de divisão
st.divider()
# Uma nova sub seção do header
st.subheader('Agendamento Cronológico')

# st.date_input()
data_inicio = st.date_input(
    label='Data de mobilização',
    value=datetime.date.today(),
    format='DD/MM/YYYY',
    key='data_mobilizacao'
)

# st.datetime_input()
data_hora_limete = st.datetime_input(
    label='Data e hora limite para reporte:',
    # Inicialização como o momento atual
    value='now',
    format="DD/MM/YYYY",
    step=datetime.timedelta(minutes=15),
    key='datetime_limite',
    help='Define o prazo final para submissão do relatório.'
)

# Escrever a saída
st.write(f"Início: {data_inicio} | Prazo final: {data_hora_limete.strftime('%d/%m/%Y %H:%M')}")

# Implementação de widget binding para persistência via URL
# Linha de divisão
st.divider()
# Uma nova sub seção do header
st.subheader('Persistência e Compartilhamento')

# Widget vinculado aos parâmetros da URL
regiao_foco = st.pills(
    label='Região de monitoramento (sincronizada):',
    options=['Fronteira', 'Deserto', 'Floresta', 'Costa'],
    key='regiao_foco',
    bind='query-params'
)

# Escrever a saída
st.write(f'Você está monitorando a região: **{regiao_foco}**')
         

