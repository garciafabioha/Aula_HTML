# --- Importar o Streamlit --- #
import streamlit as st

# --- Título da página --- #
st.title('Meu Perfil')

# --- Cabeçalho com as boas vindas --- #
st.header('Seja bem-vindo ao meu site! 👋')

# --- Subcebeçalho com o nome --- #
st.subheader('Sou o Gui!')

# --- Usar o st.markdown() para as informações do perfil --- #
st.markdown('''
Sou formado em **Biotecnologia** 🧬 e Mestre em  **Bioinformática** 🖥️
Gosto muito de *Python*, utilizo ele para tudo!
As áreas que gosto de estudar são:
* Análise de dados;
* Inteligência artificial;
* Visão computacional;
* Automação;
* E claro, **Streamlit**!
''')

# --- Usar o st.write() --- #
st.write('Espero que tenha gostado do meu perfil!')