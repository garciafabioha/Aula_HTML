# Exercício 1: Relatório de Margem de Lucro (Setor Financeiro)
# Uma empresa de varejo precisa de um resumo rápido sobre a performance de um produto.
# Dado o faturamento de R$ 45.000,00 e o custo de R$ 23.500,00,
# crie um programa que calcule o lucro e a margem de lucro (lucro dividido pelo faturamento).
# Exiba uma mensagem formatada onde o lucro use o separador de milhar e duas casas decimais,
# e a margem seja exibida como uma porcentagem inteira.
# dado_fat = 45000
# custo = 23500
# luc_liq = custo / dado_fat 
# print(f"Lucro Líquido: {luc_liq:.2%}")
# print(f"Margem em percentual inteiro: {luc_liq:.0%}")

# Exercício 2: Padronização de Dados de CRM (Setor de Vendas)
# Um vendedor cadastrou um cliente com os dados desorganizados no sistema:
# nome = " mArCoS aNtOnIo rOcHa " e email = " MARCOS.ROCHA@GMAIL.COM ". Para evitar duplicidade e erros de envio, você deve:
# Remover os espaços extras no início e fim das duas variáveis.
# Deixar o nome apenas com as primeiras letras de cada palavra em maiúsculo (formato de nome próprio).
# Deixar o e-mail todo em letras minúsculas. Exiba os resultados finais no console.
# texto.strip()   # Remove espaços dos dois lados
# texto.lstrip()  # Remove apenas do lado esquerdo (início)
# texto.rstrip()  # Remove apenas do lado direito (final)
# nome = " mArCoS aNtOnIo rOcHa "
# email = " MARCOS.ROCHA@GMAIL.COM "
# print(nome.strip().title())   # Remove espaços + formata nome próprio
# print(email.strip().lower())  # Remove espaços + tudo minúsculo

# Exercício 3: Migração de Servidor de E-mail (Setor de TI)
# Sua empresa mudou de nome e todos os funcionários que usavam o 
# domínio @empresa.com.br agora devem usar o 
# domínio @grupocorp.com.
# O e-mail do funcionário é andre_silva@empresa.com.br.
# Crie um código que substitua automaticamente o domínio antigo pelo novo e exiba o novo endereço de e-mail.

# Exercício 4: Extração de Username para Log (Setor de Segurança)
# Para criar um log de acessos, o sistema precisa extrair apenas a
# parte do nome do usuário de um e-mail corporativo (tudo o que vem antes do @).
# Dado o e-mail beatriz.oliveira@grupocorp.com, use a função .find()
# e o fatiamento de texto para extrair e exibir apenas o nome beatriz.oliveira.
# email = "beatriz.oliveira@grupocorp.com"
# antes_arroba = email.find("@")   
# posicao_ant = email[0:antes_arroba] # acha a posição do @         
# print(f"Usuário: {posicao_ant}")
# antes_arroba = email.split("@")     # ['beatriz.oliveira', 'grupocorp.com']
# print(f"Usuário: {antes_arroba}")
# antes_arroba = email.split("@")[0]  # 'beatriz.oliveira' → índice 0
# print(f"Usuário: {antes_arroba}")
# antes_arroba = email.split("@")[1]  # 'grupocorp.com'    → índice 1
# print(f"Usuário: {antes_arroba}")

# Exercício 5: Personalização de E-mail de Marketing (Setor de Marketing)
# O marketing quer enviar um e-mail de boas-vindas. O cliente forneceu o nome completo:
# lucas ferreira souza. Você deve extrair apenas o primeiro nome para usar na saudação (ex: "Olá, Lucas!"). O código deve:
# Encontrar a posição do primeiro espaço.
# Fatiar o texto para pegar apenas o primeiro nome.
# Formatar o nome com a primeira letra maiúscula.
# Exibir a mensagem: "Olá, [Primeiro Nome], seja bem-vindo ao nosso clube!"
# nome_completo = "lucas ferreira souza"
# pos_espaco = nome_completo.find(" ")
# print(f"Posição do primeiro espaço: {pos_espaco}") 
# first_name = nome_completo.split()[0]  # divide por espaço e pega o índice 0
# print(f"Olá, {first_name.title()}!")   # .title() para maiúscula no início
# print(f"Olá, {first_name.title()}, seja bem-vindo ao nosso clube!")

