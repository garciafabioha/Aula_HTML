faturamento = 1000
custo = 300

lucro = faturamento - custo

print("O lucro foi de", lucro, "e o faturamento foi de", faturamento)
mensagem = "O lucro foi de " + str(lucro) + " e o faturamento foi de " + str(faturamento)

print(mensagem)
# f-string
texto = f"O lucro foi de R${lucro} e o faturamento foi de R${faturamento}"
print(texto)

# formulas/funções de texto
email = "EMAIL_NOVO@gmail.com"

email = email.lower() # coloca em letra minúscula
email = email.upper() # coloca em letra maiúscula

print(email)

# tamanho de um texto
tamanho_texto = len(email)
print(tamanho_texto)

# posição de um caracter no texto
posicao = email.find("@")
print(posicao)

# pedaços de um texto
nome_usuario = email[:posicao]
print(nome_usuario)

# trocar um pedaço de texto
email = email.lower()
email = email.replace("gmail.com", "yahoo.com")
print(email)

# title, capitalize, upper
nome = "joão lira"
print(nome.capitalize()) # colocar a 1ªletra maiúscula
print(nome.title()) # coloca a 1ªletra de cada palavra maiúscula
print(nome.upper()) # coloca tudo maiúsculo
print(nome)