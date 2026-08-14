# if condicao/comparação:
#     tudo o que você quer que aconteça se essa condição for verdadeira
# else:
#     caso o contrario, ele vai executar o que está aqui

vendas = 600
meta = 500

if vendas >= meta:
    print("Batemos a meta de vendas")
    if vendas >= (2 * meta):
        print("Foi muito fácil, batemos mais que o dobro da meta")
    else:
        print("Passamos por pouco da meta")
else:
    vendas_faltantes = meta - vendas
    print(f"Faltaram {vendas_faltantes} vendas")

# faixas de bonus
# 50 se ele bateu a meta
# 100 se ele bateu mais que o dobro da meta
# 0 se ele não bateu a meta
meta_funcionario = 500
vendas_funcionario = 497

if vendas_funcionario >= (2 * meta_funcionario):
    bonus = 100
elif vendas_funcionario >= meta_funcionario:
    bonus = 50
else:
    bonus = 0 

print(bonus)

# cadastro de produtos
lista_produtos = ["iphone", "mac", "apple watch", "airpod"]

produto_a_cadastrar = input("Digite o nome do produto:")
produto_a_cadastrar = produto_a_cadastrar.lower()

if produto_a_cadastrar in lista_produtos:
    print("Produto já cadastrado")
else:
    lista_produtos.append(produto_a_cadastrar)

print(lista_produtos)

# mais de 1 condição

meta_empresa = 500
meta_funcionario = 50
vendas_empresa = 450
vendas_funcionario = 51

if vendas_funcionario >= meta_funcionario and vendas_empresa >= meta_empresa:
    print("Vai ganhar bonus")
else:
    print("Sem bonus")