faturamento = input("Digite o faturamento desse mês:") # sempre vem uma string
# R$800
faturamento = faturamento.replace("R$", "").replace(" ", "") # "800"
faturamento = float(faturamento)  # 800

print(faturamento)

custo = 300

lucro = faturamento - custo
print(f"O faturamento foi de {faturamento} e o lucro foi de {lucro}")