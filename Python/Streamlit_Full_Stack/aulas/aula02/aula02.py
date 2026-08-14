# --- Importar as bibliotecas
import numpy as np
import pandas as pd
from fpdf import FPDF
import streamlit as st


def gerar_pdf():
    st.success("PDF gerado com sucesso!")

# --- Configuração inicial da página para permitir a estruturação
st.set_page_config(
    page_title="Aula 02: Layouts",
    layout='wide'    
)

# --- Título da Página
st.title('🚀 Aula 02: Estruturação Espacial')
st.markdown('''Nesta Aula, contruiremos um dashboard modular. O código evoluirá a cada seção.
             adiconando camadas de complexidade até termos uma aplicação **completa** e *funcional*. ''')

# --- Base de dados para utilizar nas visualizações
dados = pd.DataFrame(
    np.random.randn(20,5),
    columns=['Vendas', 'Lucro', 'Meta', 'Custo', 'Retorno']
)
st.header('O poder das colunas e alinhamento vertical')

# --- Criar colunas com pesos/tamanhos diferentes
colunas = st.columns(
    spec=[1, 3, 1],
    gap='medium', # controle o espaçamento entre as colunas
    vertical_alignment='center', # garante que os widgets fiquem visualmente equilibrados
    border=True # adicionar bordar ás colunas
)

# --- Adicionar informações nas colunas
with colunas[0]:
    st.subheader('Indicadores')
    st.metric(
        label='Vendas Totais',
        value='R$ 1.250.00',
        delta='12%'
    )
    st.metric(
        label='Lucro Líquido',
        value='R$ 450.00',
        delta='-3%'        
    )
with colunas[1]:
        st.subheader('Análise Visual') 
        st.line_chart(dados)
with colunas[2]:
        st.subheader('Ações') 
        st.button('Atualizar Dados', key='atualizar_dados', use_container_width=True)  
        if st.button('Exportar PDF', key='exportar_pdf', use_container_width=True):
            gerar_pdf()
        modo = st.checkbox('Habilitar Modo Noturno', key='modo_noturno')   
        if modo:
            st.write("Modo noturno ligado")
        else:
            st.write("Modo claro")
      
st.divider()  

st.header('Containers dinâmicos e layout horizontal')
# --- Criar um container que se compara como uma barra de ferramentas
st.write('Configurações da seção:')
barra_ferramentas = st.container(
     horizontal=True, # alinha os elementos internamente em linha
     border=True,
     width='content', # o conteiner ocupa o espaço necessário
     horizontal_alignment='left'    
)

# --- Colocar o container
with barra_ferramentas:
     st.toggle('Filtrar finais de semana', key='filtro_fim_semana')
     st.toggle('Mostrar médias', key='mostrar_medias')
     st.segmented_control(
          label='Escala',
          options=['Diário', 'Semanal', 'Mensal'],
          default='Diário'
     )

# --- Container para exibição de status, utilizando a largura total padrão stretch
with st.container(border=True):
     st.info('Esse container demonstra como o conteúdo adapta-se á largura total disponível.')
     st.write('Este bloco pode conter qualquer tipo de widget, como tabelas ou texto longos.')

st.divider()  

st.header('Profundidade de interface como abas reativas')

# --- Criar abas que rastreiam seu estado através de uma chave (key)
abas = st.tabs(
     tabs=['Visualização', 'Dados Brutos', 'Configurações'],
     on_change='rerun', # habilita a propriedade .open em cada aba
     key='navegacao_principal'
)

#--- Adicionar informações ás abas
with abas[0]:
     # --- A propriedades .open permite executar a lógica condicional de alta performace
     if abas[0].open:
          st.write('Renderizando visualização complexa sob demanda...')
          colunas = st.columns(2, gap='large')
          with colunas[0]:
               st.bar_chart(dados['Vendas'])
          with colunas[1]:
               st.area_chart(dados['Lucro'])

with abas[1]:
     if abas[1].open:
          st.write('Exibindo dados brutos da operação:')
          st.dataframe(dados.style.highlight_max(axis=0), width='stretch')  

with abas[2]:
     if abas[2].open:
          st.write('Painel de controle de administrador')
          st.slider('Ajustar limite de alerta', min_value=0, max_value=100, value=50)
          
st.divider()  

st.header('Revelação progressiva e popovers')   

# --- Criar um popover para filtros avançados que não precisa ocupar espaço fixo
# --- O popover fluta sobre o conteúdo, ideal para menus de configurações
with st.popover('🔍 Filtros avançados e explicações', icon='🛠️'):
     st.write('Use os campos abaixo para refinar sua análise:')
     st.date_input('Filtrar por período', value=None, format="DD/MM/YYYY")
     st.multiselect('Selecionar regiões', options=['Norte', 'Sul', 'Leste', 'Oeste'])

     # --- Podemos alinha em estrutura simples para organização interna
     with st.expander('Ver glossário de termos:'):
          st.caption('Vendas: Valor bruto faturado no período.')
          st.caption('Lucro: Valor líquido após deduções operacionais:')

# --- Exemplo de st.expander() que reage na abertura
def abrir_detalhes():
     st.toast('Você está visualizando os detalhes técnicos', icon='👀')

with st.expander('📄 Detalhes de auditoria (clique para ver)', on_change=abrir_detalhes):
     st.write(f'Timestamp da última atualização: {pd.Timestamp.now().strftime('%d/%m/%Y %H:%M:%S')}.')
               
