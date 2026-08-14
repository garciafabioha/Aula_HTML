# for item in lista:
#    execute isso para cada item

lista_produtos = ["iphone", "mac", "apple watch", "airpod"]

for item in lista_produtos:
    print(item)


# for com intervalo fixo
for i in range(10):
    print("Se inscreve no canal")
    

# for para percorrer uma lista
lista_precos = [10000, 15000, 5000, 2000]
inflacao = 0.1

nova_lista = []

for preco in lista_precos:
    novo_preco = preco * (1 + inflacao)
    nova_lista.append(novo_preco)

print(nova_lista)

# for para percorrer um dicionario de valores
dic_produtos = {"iphone": 10000, "mac": 15000, 
                "apple watch": 5000, "airpod": 2000}

for item in dic_produtos:
    novo_preco = dic_produtos[item] * 1.1
    dic_produtos[item] = novo_preco
print(dic_produtos)

# while

# vendas = 100
# meta = 200

# while vendas < meta:
#     print("Não bateu a meta")
#     vendas = vendas + 10