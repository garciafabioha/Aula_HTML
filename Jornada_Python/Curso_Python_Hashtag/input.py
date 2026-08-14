#Exercício 1: Calculadora de Imposto sobre Vendas (Setor Fiscal)
# Uma empresa de serviços precisa calcular o imposto de 15% sobre o valor bruto de uma nota fiscal.
# Como o valor muitas vezes vem copiado de planilhas com "R$" e vírgula, seu programa deve:
# Pedir para o usuário digitar o valor bruto (Ex: R$ 5.000,00).
# Limpar o texto removendo o "R$" e trocando a vírgula por ponto.
# Converter para número decimal (float).
# Calcular o valor do imposto (15% do valor bruto).
# Exibir uma mensagem formatada com f-string mostrando o valor do imposto com duas casas decimais.
# imp = 0.15
# vlr_bruto = input("Digite o valor bruto (Ex: R$ 5.000,00): ")
# vlr_limpo = vlr_bruto.replace("R$", "").replace(".", "").replace(",", ".").strip()
# vlr_num = float(vlr_limpo)
# vlr_imp = vlr_num * imp
# print(f"Valor do Imposto: R$ {vlr_imp:,.2f}")

# Exercício 2: Sistema de Cadastro de Colaborador (Setor de RH)
# Ao cadastrar um novo funcionário,
# o RH precisa extrair o primeiro nome para criar um crachá e padronizar o e-mail. Crie um programa que:

# Peça o nome completo do colaborador.
# Peça o e-mail pessoal do colaborador.
# Extraia o primeiro nome (deixe-o com a primeira letra maiúscula).
# Padronize o e-mail (remova espaços extras e deixe tudo em letras minúsculas).
# Exiba a mensagem: "Cadastro concluído: [Primeiro Nome]. E-mail de acesso: [E-mail padronizado]".
# nome_compl = input("Favor digitar o nome completo do colaborador: ")
# email_pes = input("Favor digitar o e-mail pessoal do colaborador: ")
# print(f"\nNome: {nome_compl.title()}")
# print(f"E-mail: {email_pes.lower()}")
# first_name = nome_compl.split()[0] 
# print(f"{first_name.title()}")
# print(f"Cadastro concluído: {first_name.title()}. E-mail de acesso: {email_pes}")

# Exercício 3: Análise de Metas de Vendas (Setor Comercial)
# Um gerente quer comparar o desempenho de duas filiais. O programa deve:
# Pedir o faturamento da Loja A e o faturamento da Loja B (o usuário pode digitar números decimais).
# Calcular o faturamento total das duas lojas.
# Calcular a média de faturamento entre elas.
# Exibir uma única mensagem formatada informando o total e a média, utilizando o separador de milhar e duas casas decimais.
# fat_loja_a = int(input("Digite faturamento da loja A: "))
# fat_loja_b = int(input("Digite faturamento da loja B: "))

# fat_total = fat_loja_a + fat_loja_b
# media = fat_total / 2
# print(f"Total faturamento da loja A e loja B: R$ {fat_total:.2f}")
# print(f"Total da média de faturamente da loja A e loja B: R$ {media:.2f}")