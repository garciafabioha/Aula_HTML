#lista
lista_nova = []
nomes = ["Lira", "Fábio"]
print(nomes)
#add na lista
nomes.append("Maria")
print(nomes)
#pegar informação da lista posições
print(nomes[0])

#dicionário = mensagem no Python
idades = {"Lira":31, "Fábio":54}
print(idades["Fábio"]) #pergar a informação do dicionário
#add no dicionário
idades["Fábio"] = 55
print(idades)

# role = qwuem é o usuário
# content = conteúdo da mensagem
mensagem1 = {"role": "assistant", "content": "Bora aprender Python"}
mensagem2 = {"role": "user", "content": "Bora sim, bora aprender"}
mensagem3 = {"role": "assistant", "content": "Então vamos começar a aula"}

lista_mensagens = [mensagem1, mensagem2, mensagem3]

nova_mensagem = {"role": "user", "content": "Opa, agora bora Python"}

lista_mensagens.append(nova_mensagem)

print(lista_mensagens)