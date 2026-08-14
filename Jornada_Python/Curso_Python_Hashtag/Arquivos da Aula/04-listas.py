lista_nomes = ["Lira", "Alon", "João", "Nayra", "Manu"]

# tamanho da lista
print(len(lista_nomes))

# pegar um item da lista - sempre pela posição do elemento
primeiro = lista_nomes[0]
print(primeiro)

# encontrar um item na lista
existe_na_lista = "Lira" in lista_nomes
print(existe_na_lista)

posicao_lira = lista_nomes.index("Lira")
print(posicao_lira)

# outro exemplo
lista_vendas = [100, 50, 1000, 800, 35]

# total
total_vendas = sum(lista_vendas)
print("Total de vendas", total_vendas)

# maior valor
maior_valor = max(lista_vendas)

# menor valor
menor_valor = min(lista_vendas)

# media de vendas
media_vendas = total_vendas / len(lista_vendas)

print("Maior valor", maior_valor)
print("Menor valor", menor_valor)
print("Média", media_vendas)

# outro exemplo

lista_precos = [5000, 3000, 2000]
novo_valor = lista_precos[0] * 1.1
lista_precos[0] = novo_valor
print(lista_precos)

# adicionar um elemento
lista_precos.append(600)
print(lista_precos)

# remover um elemento
lista_nomes.remove("Lira")
print(lista_nomes)

# juntar duas listas
novas_contratacoes = ["Diego", "Mirele"]
lista_nomes.extend(novas_contratacoes)
print(lista_nomes)

# ordenar uma lista
lista_precos.sort(reverse=True)
print(lista_precos)