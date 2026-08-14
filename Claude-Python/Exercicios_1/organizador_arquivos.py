# 1. Manipulação de arquivos
# **Organizador de arquivos por extensão**

# Blioteca para trabalhar com caminho de pasta, copiar, mover e deltar arquivos
import shutil
# Blioteca para trabalhar com caminho de pasta
from pathlib import Path

caminho = input("Informe o caminho da pasta: ")

pasta = Path(caminho)

if not pasta.exists():
    print("A pasta informada não existe.")
    exit()

if not pasta.is_dir():
    print("O caminho informado não é uma pasta.")
    exit()

print("Pasta encontrada:", pasta)

for arquivo in pasta.iterdir():

    if arquivo.is_file():

        print("Arquivo:", arquivo.name)
        print("Extensão:", arquivo.suffix)

        # lstrip()   # remove do lado esquerdo
        # rstrip()   # remove do lado direito
        # strip()    # remove dos dois lados
        # removeprefix(".") tira esse ponto do começoe e sem o efeito colateral de continuar removendo caracteres repetido
        extensao = arquivo.suffix.removeprefix(".")

        if extensao == "":
            extensao = "sem_extensao"

        pasta_destino = pasta / extensao

        pasta_destino.mkdir(exist_ok=True)

        print("Pasta destino:", pasta_destino)

        destino_arquivo = pasta_destino / arquivo.name

        # Move o arquivo conforme extensão para sua pasta específica
        shutil.move(arquivo, destino_arquivo)