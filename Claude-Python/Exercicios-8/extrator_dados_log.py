import re
from collections import Counter

# Expressão regular
padrao = re.compile(
    r"(\d{4}-\d{2}-\d{2}) "
    r"(\d{2}:\d{2}:\d{2}) "
    r"(ERROR|INFO|WARNING|DEBUG) "
    r"(.*)"
)

registros = []

# Abrir e ler o arquivo
with open("log.txt", "r", encoding="utf-8") as arquivo:

    for linha in arquivo:

        linha = linha.strip()

        resultado = padrao.match(linha)

        if resultado:

            data, hora, nivel, mensagem = resultado.groups()

            registro = {
                "data": data,
                "hora": hora,
                "nivel": nivel,
                "mensagem": mensagem
            }

            registros.append(registro)


# Mostrar todos os registros
print("\nTODOS OS REGISTROS:")

for registro in registros:
    print(registro)


# Filtrar somente ERROR
erros = [
    registro
    for registro in registros
    if registro["nivel"] == "ERROR"
]

print("\nSOMENTE ERROS:")

for erro in erros:
    print(
        erro["data"],
        erro["hora"],
        erro["mensagem"]
    )

# BÔNUS - quantidade de erros por hora
erros_por_hora = Counter(
    erro["hora"][:2]
    for erro in erros
)

print("\nERROS POR HORA:")

for hora, quantidade in erros_por_hora.items():
    print(f"{hora}h: {quantidade} erro(s)")