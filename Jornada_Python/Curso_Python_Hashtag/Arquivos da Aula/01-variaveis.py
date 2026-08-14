
faturamento = 997 # numeros inteiros -> int
custo = 300
imposto = 0.2 # float
lucro1 = faturamento - custo - imposto * faturamento

faturamento = 600
lucro2 = faturamento - custo - imposto * faturamento
print(lucro1)
print(lucro2)

# tipos de variáveis
# int -> numeros inteiros
# float -> numeros com casa decimal
# string -> textos (str)
# booleanos -> Verdadeiro ou Falso (True / False)

print("O lucro da loja no primeiro mês foi de", lucro1)
print("O lucro da loja no segundo mês foi de", lucro2)

print("O lucro da loja foi de", lucro1, "para o primeiro mês")

margem_lucro = lucro2 / faturamento

print("Margem de lucro de", margem_lucro)

meta = 0.5

bateu_meta = margem_lucro >= meta # booleana
print(bateu_meta)

# mod % (resto da divisão)
# // (parte inteira da divisão)
duracao_contrato = 140 # meses

anos = duracao_contrato // 12
meses_sobra = duracao_contrato % 12

print("O contrato tem", anos, "anos e", meses_sobra, "meses")

