# Classe de Produto
class Produto:

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f} - Quantidade: {self.quantidade}"


# Classe de Estoque
class Estoque:

    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)


# Criando os produtos
produto1 = Produto("Notebook", 3500.00, 5)
produto2 = Produto("Mouse", 80.00, 10)


# Criando o estoque
estoque = Estoque()


# Adicionando os produtos ao estoque
estoque.adicionar_produto(produto1)
estoque.adicionar_produto(produto2)


# Mostrando os produtos do estoque
for produto in estoque.produtos:
    print(produto)

print("Teste Git")