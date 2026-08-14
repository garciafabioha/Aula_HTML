# Exercício 1: Cálculo de Bônus de Vendas (RH/Vendas)
# Cenário: Uma empresa decidiu dar um bônus de 10% sobre o faturamento total para a equipe de vendas. 
# Objetivo: Calcule o valor do bônus e o faturamento final da empresa após subtrair esse bônus.

# perc_bonus = 0.10
# fat_inicial = 50000
# vlr_bonus = fat_inicial * perc_bonus
# fat_final = fat_inicial - vlr_bonus

# print(f"Bônus: R$ {vlr_bonus:.2f}")
# print(f"Faturamento Fiinal: R$ {fat_final:.2f}")

# Exercício 2: Controle de Estoque de E-commerce (Logística)
# Cenário: Um e-commerce começou o dia com 250 unidades de um smartphone no estoque.
# Durante o dia, foram vendidos 78 unidades e chegaram mais 100 unidades de um fornecedor.
# Objetivo: Atualize a variável de estoque e exiba o saldo final.

# unid_smartphone = 250
# venda_smartphone = 78
# entrada_smartphone = 100

# estoque = unid_smartphone - (venda_smartphone - entrada_smartphone)
# print(f"Estoque Atual é:", estoque)

# Exercício 3: Divisão de Cargas (Logística/Transporte)
# Cenário: Uma transportadora precisa levar 1.250 caixas em caminhões pequenos.
# Cada caminhão suporta exatamente 12 caixas.
# Objetivo: 1. Quantos caminhões sairão totalmente cheios? (Use //)
# 2. Quantas caixas sobrarão para serem enviadas em uma última viagem menor? (Use %)
# cam_peq = 1250
# cad_cam = 12
# total_cam = cam_peq // cad_cam
# caixas_restantes = cam_peq % cad_cam
# import math
# print(f"Total de Caminhões para Transportar 1250 caixas, são: {math.ceil(total_cam)}")

# Exercício 4: Análise de Margem de Lucro (Financeiro)
# Cenário: Uma consultoria faturou R$ 15.000,00 em um projeto.
# Os custos fixos foram de R$ 5.000,00 e o imposto sobre o faturamento é de 15%.
# Objetivo: Calcule o imposto, o lucro líquido e a margem de lucro (Lucro / Faturamento).
# No final, crie uma variável booleana chamada meta_atingida que verifica se a margem de lucro é superior a 0.30 (30%).

# fat_proj = 15000
# cus_proj = 5000
# imp_fat_proj = 0.15
# vlr_imp = 15000 * 0.15
# print(f"Valor do Imposto de 15% sobre o Faturamento é: {vlr_imp:.2f}")
# luc_liq = fat_proj - vlr_imp
# print(f"Valor Líquido do Faturamento é: {luc_liq:.2f}")
# mar_luc = luc_liq / fat_proj
# print(f"Porcentagem do Lucro Líquido: {mar_luc}%")

# if mar_luc >= 0.30:
#     print(True)
# else:
#     print(False)

# Exercício 5: Conversão de Tempo de Contrato (Gestão de Projetos)
# Cenário: Um contrato de manutenção de software tem a duração de 40 meses.
# O cliente quer ver esse tempo no formato: "X anos e Y meses".
# Objetivo: Utilize os operadores de divisão inteira e resto da divisão para converter os 40 meses.
# cont_dur = 40 # meses
# meses = 12
# anos_x = cont_dur // meses # divisão inteira → anos
# print(f"Contrato em anos: {anos_x}")
# meses_y = cont_dur % meses   # resto da divisão → meses restantes
# print(f"Contrato em meses: {meses_y}")

