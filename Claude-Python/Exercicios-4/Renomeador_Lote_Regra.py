#Renomeador em lote com regras
from pathlib import Path
from datetime import datetime

caminho = input("Informe o caminho da pasta: ")

pasta = Path(caminho)

# glob - usado para procurar arquivos e pastas que correspondam a um padrão.
for arquivo in pasta.glob("*.txt"):

    # informações do sistema sobre um arquivo ou pasta, como tamanho, data de modificação e outros metadados.
    data_modificacao = arquivo.stat().st_mtime

    # um método da classe datetime que converte um timestamp em uma data e hora compreensível.
    data = datetime.fromtimestamp(data_modificacao)

    data_formatada = data.strftime("%d-%m-%Y")

    novo_nome = f"{data_formatada}_{arquivo.name}"

    print("Arquivo atual:", arquivo.name)
    print("Novo nome:", novo_nome)