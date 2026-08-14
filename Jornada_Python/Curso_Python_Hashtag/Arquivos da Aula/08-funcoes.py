# forma mais basica
def se_inscrever_canal():
    print("Se inscreve no canal")
    print("Dá o like no vídeo")

se_inscrever_canal()



dic_produtos = {"iphone": 10000, "mac": 15000, 
                "apple watch": 5000, "airpod": 2000}

def calcular_novo_preco(preco):
    # definir tudo o que eu preciso fazer para definir um novo preço
    inflacao = 0.05
    iss = 0.07
    novo_preco = preco * (1 + (inflacao + iss))
    return novo_preco


for item in dic_produtos:
    preco_original = dic_produtos[item]
    novo_preco = calcular_novo_preco(preco_original)
    dic_produtos[item] = novo_preco

print(dic_produtos)

