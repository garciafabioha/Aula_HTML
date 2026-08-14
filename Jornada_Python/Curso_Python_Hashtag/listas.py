# Exercício 1: Dashboard de Vendas (Análise de Dados)
# Você recebeu uma lista com as vendas diárias de uma equipe: vendas = [1500, 2000, 800, 3500, 1200].
# Crie um programa que exiba um pequeno relatório contendo:

# O total de vendas na semana.
# A média de vendas diária.
# O valor da melhor venda e da pior venda do período.
# mudar formato Brasil de valor com .
# def formato_br(valor):
#     return f"{valor:,.2f}".replace(",", ".")

# lista = [1500, 2000, 800, 3500, 1200]
# total_vendas =  sum(lista)
# # len() retorna a quantidade de elementos de uma lista
# media = total_vendas / len(lista) 
# # max busca o maior
# melhor = max(lista)
# # min busca o menor
# pior = min(lista)

# print("===== RELATÓRIO DE VENDAS =====")
# print(f"Total de vendas na semana: R$ {formato_br(total_vendas)}")
# print(f"Média de vendas diária:    R$ {formato_br(media)}")
# print(f"Melhor venda do período:   R$ {formato_br(melhor)}")
# print(f"Pior venda do período:     R$ {formato_br(pior)}")
# print("================================")

# Exercício 2: Gestão de Estoque (Edição e Verificação)
# Uma loja de eletrônicos possui os seguintes produtos:
# estoque = ["monitor", "teclado", "mouse", "headset"]. O gerente pediu para:

# Adicionar o item "webcam" ao final da lista.
# O "teclado" teve seu nome atualizado para "teclado mecanico". Faça essa alteração na lista.
# Verificar se "impressora" está no estoque. O programa deve exibir True ou False.
# Remover o "mouse" da lista, pois saiu de linha.

# estoque = ["monitor", "teclado", "mouse", "headset"]
# estoque.append("webcam")
# #estoque.insert(0, "webcam")  # insere na posição 0 (início)
# # ['webcam', 'monitor', 'teclado', 'mouse', 'headset']
# #nome = "teclado" 
# #nome = nome + " mecanico"
# # índice 1 = "teclado"
# estoque[1] = "teclado mecanico"  
# # in retorna True ou False
# if "impressora" in estoque:
#     print("Produto encontrado! - True")
# else:
#     print("Produto não encontrado! - False")
# # remove o item na posição 2 (mouse)
# estoque.pop(2)  
# print(estoque)

# Exercício 3: Organização de Preços (Ordenação e Slicing)
# Uma importadora listou os preços de frete em dólar:
# fretes = [50, 80, 20, 150, 40]. Para apresentar em uma reunião, você deve:
# Ordenar a lista do maior para o menor preço.
# Pegar os 2 fretes mais caros (usando fatiamento/slicing) e armazenar em uma nova lista chamada top_fretes.
# Exibir a lista original ordenada e a lista dos top_fretes.

# fretes = [50, 80, 20, 150, 40]
# # do maior para menor
# fretes.sort(reverse=True)
# # pegar os 2 fretes mais caros
# top_fretes = fretes[:2]
# # do menor para maior
# fretes.sort()
# top_fretes.sort()
# print(fretes,top_fretes)

# Exercício 4: Sistema de Logística (Busca e Extensão)
# A empresa "LogTrack" tem uma rota de entregas: rota = ["Sao Paulo", "Campinas", "Jundiai", "Sorocaba"].
# Novas cidades foram adicionadas por uma empresa parceira: novas_cidades = ["Itu", "Valinhos"]. Seu script deve:

# Unir as duas listas em uma só (usando extend).
# Identificar em qual posição (índice) está a cidade de "Sorocaba".
# Exibir a lista completa e a posição encontrada.
# Exibir uma mensagem final: “Sorocaba é a Xª cidade da rota”

# rota = ["Sao Paulo", "Campinas", "Jundiai", "Sorocaba"]
# novas_cidades = ["Itu", "Valinhos"]
# # uni as duas listas em uma única lista
# rota.extend(novas_cidades)
# print(rota)
# # Identificar em qual posição (índice) está a cidade de "Sorocaba".
# posicao = rota.index("Sorocaba")
# print(f"Lista completa: {rota}")
# print(f"Sorocaba está na posição: {posicao} da rota")

# Exercício 5: Atualização de Preços Interativa
# (Input + Lista) Você tem uma lista de preços de produtos:
# precos = [100.0, 250.0, 500.0] e uma com o nome:
# vinhos = ["Branco", "Tinto","Champagne"].
# Crie um programa interativo que:

# Peça para o usuário digitar qual o nome do produto.
# Peça para o usuário digitar o novo preço.
# Atualize o preço na lista e exiba as listas completas com os nomes e os preços
#precos = [100.0, 250.0, 500.0]
# vinhos = ["Branco", "Tinto","Champagne"]
# print(precos,vinhos)
# nome = input("Digite o nome do produto: ")
# preco = float(input("Digite o novo preço: R$ "))
# # in unir as duas listas
# if nome in vinhos:
#     posicao = vinhos.index(nome)
#     precos[posicao] = preco
#     print("\nPreço atualizado com sucesso!")
# else:
#     print("\nProduto não encontrado na lista!")

# print("\n===== LISTA DE VINHOS =====")
# # zip uni as duas listas
# for i in range(len(vinhos)):
#     print(f"{vinhos[i]}: R$ {precos[i]:.2f}")






