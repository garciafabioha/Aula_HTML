# Cadastrar um produto
# Repitir o passo 4 até acabar o cadastro dos produtos

# pyautogui.click - click
# pyautogui.write - escreve um texto
# pyautogui.press - aperta uma tecla
# pyautogui.hotkey - aperta um atalho (hotkey)

import pyautogui
import time
time.sleep(5)
import pandas
from pathlib import Path

pyautogui.PAUSE = 1

# Entrar no sistema da empresa
# abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Acessar o sistema
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
# Fazer uma pausa maior
time.sleep(3)
# Fazer login
email = "pythonimpressionador@gmail.com"
senha = "sua senha muito muito muito dificilima"
pyautogui.click(x=595, y=494)
pyautogui.write(email)
# pular para outro campo
pyautogui.press("tab")
pyautogui.write(senha)
# pular para outro campo
pyautogui.press("tab")
pyautogui.press("enter")
# Fazer uma pausa maior
time.sleep(3)
# Abrir a base de dados
BASE_DIR = Path(__file__).parent   
tabela = pandas.read_csv(BASE_DIR / "produtos.csv")
print(tabela)

#Loop correto
for linha in tabela.index:   
    pyautogui.click(x=589, y=367) #clicar no campo do código
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo) 
    pyautogui.press("tab") #passar para próximo campo
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca) 
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")  
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab") 
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")  
    #passar para botão enviar
    pyautogui.press("enter")  
    #voltar para início da tela
    pyautogui.scroll(5000)