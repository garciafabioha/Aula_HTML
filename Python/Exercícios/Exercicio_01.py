#1
faturamento = 50000
perc_bonus = 0.1
bonus_total = faturamento * perc_bonus
faturamento_liquido = faturamento - bonus_total
print("FaturamentO Líquido", faturamento_liquido)
print("Bonus Total", bonus_total)

#2
estoque = 250
vendas = 78
reposicao = 100
estoque = estoque - vendas + reposicao
print("Estoque Final", estoque)

#3
import math
caixa = 1250
caminhao = 12
caminhao_completo = caixa / caminhao
print("Transporte de Total de Caixas", math.ceil(caminhao_completo))

#4
faturamento = 15000
custo = 5000
imposto_percentual = 0.15

imposto = faturamento * imposto_percentual
print("Imposto", imposto)
lucro_liquido = (faturamento - imposto) - custo
print("Lucro Líquido", lucro_liquido)
if faturamento != 0:
    margem = lucro_liquido / faturamento
    print(f"Margem de Lucro: {margem * 100:.2f}%")
else:
    print("Faturamento Zerado!")    