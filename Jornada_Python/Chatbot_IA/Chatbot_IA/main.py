# titulo
# input do chat
# a cada mensagem enviada:
    # mostrar a mensagem que o usuario enviou no chat
    # enviar essa mensagem para a IA responder
    # aparece na tela a resposta da IA

# streamlit - frontend e backend
# role quem é o usuário
# IA assistant
# usuário user

import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # carrega as variáveis do arquivo .env

# modelo para receber a chave do arquivo .env
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
modelo = genai.GenerativeModel("gemini-2.5-flash-lite")

st.title("Chatbot com IA")
# senão existe criar lista_mensagens vazia
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

texto_usuario = st.chat_input("Digite sua mensagem")

if texto_usuario:
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario = {"role": "user", "parts": texto_usuario} 
    st.session_state["lista_mensagens"].append(mensagem_usuario)
    #nome
    #user
    #assistant

    # resposta da IA
    chat = modelo.start_chat(history=st.session_state["lista_mensagens"])
    resposta_modelo = chat.send_message(texto_usuario)
    
    # pegar o texto da resposta
    resposta_ia = resposta_modelo.text    

    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)




