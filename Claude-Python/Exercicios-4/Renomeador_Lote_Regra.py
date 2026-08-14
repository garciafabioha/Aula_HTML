# Renomeador em lote com regras
import re
from pathlib import Path
from datetime import datetime

caminho = input("Informe o caminho da pasta: ")

pasta = Path(caminho)

modo_simulacao = True

# Procura arquivos .txt
for arquivo in pasta.glob("*.txt"):

    if arquivo.name == "log.txt":
        continue

    # Verifica se já começa com DD-MM-AAAA_
    if re.match(r"^\d{2}-\d{2}-\d{4}_", arquivo.name):
        print("Já está renomeado:", arquivo.name)
        continue

    # Pega a data de modificação
    data_modificacao = arquivo.stat().st_mtime

    # Converte timestamp para datetime
    data = datetime.fromtimestamp(data_modificacao)

    # Formato solicitado: DD-MM-AAAA
    data_formatada = data.strftime("%d-%m-%Y")

    # Cria o novo nome ANTES de utilizá-lo
    novo_nome = f"{data_formatada}_{arquivo.name}"

    # Momento da execução (usado só no log)
    agora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Cria também o caminho completo do novo arquivo
    novo_caminho = pasta / novo_nome

    if modo_simulacao:
        print("SIMULAÇÃO:")
        print(f"{arquivo.name} -> {novo_nome}")
    else:
        arquivo.rename(novo_caminho)

    with open("log.txt", "a", encoding="utf-8") as log:
        log.write(f"[{agora}] {arquivo.name} -> {novo_nome}\n")


    print(novo_caminho)