# tupla é como se fosse um lista imutável

coordenadas = (10.2534548, 1.2684865)

print(coordenadas)

# unpacking
latitude, longitude = coordenadas

print(latitude)
print(longitude)

# bonus 1: R$2 por venda -> incentiva a qtde de vendas
# bonus 2: 1% do valor de vendas -> incentiva o cara a vender produtos mais caros

vendas_funcionario = [10, 20, 50, 50, 600, 50, 60, 400]

# tuplas para funções

def calcular_bonus(lista_vendas):
    bonus1 = 2 * len(lista_vendas)
    bonus2 = 0.01 * sum(lista_vendas)
    return bonus1, bonus2

resultado_bonus = calcular_bonus(vendas_funcionario)
bonus1, bonus2 = resultado_bonus
print(bonus1)
print(bonus2)


# tuplas com o for

lista_vendas = [("Lira", 100), ("Alon", 50), ("Manu", 300)]

for vendedor, vendas in lista_vendas:
    print(f"O {vendedor} vendeu {vendas}")

