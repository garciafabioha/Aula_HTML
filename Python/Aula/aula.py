import time
# produto = "Iphone"
# quantidade_estoque = 200

# print("O produto", produto, "tem", quantidade_estoque,
#       "unidade no estoque")

# print("Contagem")
# for i in range(5):
#     print(5 - i, end="\r")
#     time.sleep(1)
# print("Acabou")

# help(print)

# def calcular_imposto(faturamento, taxa):
#     """
#     Texto teste
#     """
#     imposto = faturamento * taxa
#     return imposto
 
# valor = calcular_imposto(10000,  0.15)

# print(valor)

# lista = list(range(5))
# lista = list(range(1, 6)}
# lista = list(range(1, 10, 2))
# # lista = range(5, 0, -1)

# print(lista)

# for i in range(1, 10, 2):
#     print(i, end="\r")
#     time.sleep(1)

#salarios = [1000, 5000, 7000, 850]

# salario = float(input("Digite o Valor do Salário Atual: \n"))

# def aumentar_salario(salario):
#     if salario > 1000:
#         novo_salario = salario * 1.00
#     else:
#         novo_salario = salario * 1.1
#     return novo_salario

# for salario in salarios:
#     novo = aumentar_salario(salario)
#     print(f"R$ {salario:.2f} -> R$ {novo:.2f}")

# novos_salarios = list(map(lambda x: x * 1.1, salarios))
# print(novos_salarios)

# salarios_altos = list(filter(lambda x: x > 2000, salarios))
# print(salarios_altos)

# custos = [600, 5000, 350, 4000]
# custo_total = sum(custos,start=1000)
# print(custo_total)

# salarios_ordenados = sorted(salarios, reverse=True)
# print(custo_total)

# salarios = [(1000, 500, 180),
#             (5000, 40, 200),
#             (7000, 0, 0),
#             (600, 4000, 150)]
# funcionarios_ordenados = sorted(salarios, reverse=True, key=lambda x:
#                                 sum(x))
# print(funcionarios_ordenados)

salarios = [1000, 5000, 7000, 850]
funcionarios = ["Garcia", "Fábio", "Neide", "Matheus"]
# for i, salario in enumerate(salarios):
#     funcionario = funcionarios[i]
#     print(f"Novo salário do {funcionario} é {salario * 1.1:.2f}")
for funcionario, salario in zip(funcionarios, salarios):
    print(f"Novo salário do {funcionario} é {salario * 1.1:.2f}")

arquivo = open("salarios_funcionarios.txt", "a")




