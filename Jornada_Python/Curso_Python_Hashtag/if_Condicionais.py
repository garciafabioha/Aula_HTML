# Exercício 1: Validação de Investimento (Setor Financeiro)
# Uma corretora de valores quer automatizar a recomendação básica de perfil.
# Crie um programa que peça ao usuário o valor que ele deseja investir.

# Se o valor for menor que R$ 1.000,00, exiba: "Perfil iniciante: Sugerimos Tesouro Direto".
# Se o valor for entre R$ 1.000,00 e R$ 5.000,00 (inclusive), exiba: "Perfil moderado: Sugerimos Fundos Imobiliários".
# Se o valor for acima de R$ 5.000,00, exiba: "Perfil arrojado: Sugerimos Ações".
#  *Lembre-se de tratar o input caso o usuário digite "R$" ou use vírgula.*

# entrada = input("Valor que será investido: R$ ")
# entrada = entrada.replace("R$", "").replace(".", "").replace(",", ".").strip()
# valor_invest = float(entrada)

# if valor_invest <= 1000:
#     print(f"Perfil conservador: Sugerimos Poupança. Valor que será investido: R$ {valor_invest:.2f}")
# elif valor_invest <= 5000:
#     print(f"Perfil moderado: Sugerimos Fundos Imobiliários. Valor que será investido: R$ {valor_invest:.2f}")
# else:
#     print(f"Perfil arrojado: Sugerimos Ações. Valor que será investido: R$ {valor_invest:.2f}")

# Exercício 2: Controle de Acesso ao Sistema
# (Setor de Segurança) Você tem uma lista
# de e-mails de administradores:
# admins = ["ana@empresa.com", "guilherme@empresa.com", "felipe@empresa.com"].
# Crie um programa que peça o e-mail do usuário. O programa deve:

# Padronizar o e-mail (letras minúsculas e sem espaços).
# Verificar se o e-mail está na lista de admins.
# Se estiver, exibir: "Acesso liberado! Bem-vindo ao painel de controle".
# Caso contrário, exibir: "Acesso negado. Você não tem permissões de administrador".
# admins = ["ana@empresa.com", "guilherme@empresa.com", "felipe@empresa.com"]
# email = input("Digite seu e-mail: ")

# email = email.lower().strip().replace(" ", "")

# if email in admins:
#     print(f"Acesso liberado! Bem-vindo ao painel de controle. {email}")
# else:
#     print(f"Acesso negado. Você não tem permissões de administrador. {email}")