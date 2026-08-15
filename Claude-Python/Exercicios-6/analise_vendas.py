vendas = [
    {"produto": "Caneta", "categoria": "Papelaria", "valor": 2.5, "qtd": 10},
    {"produto": "Caderno", "categoria": "Papelaria", "valor": 15.0, "qtd": 3},
    {"produto": "Mouse", "categoria": "Eletrônicos", "valor": 45.0, "qtd": 2},
]

# 1. Calcular o total de cada venda
totais = [
    {
        "produto": venda["produto"],
        "categoria": venda["categoria"],
        "total": venda["valor"] * venda["qtd"]
    }
    for venda in vendas
]

print("TOTAIS POR PRODUTO")
print("-" * 40)

for item in totais:
    print(f'{item["produto"]}: R$ {item["total"]:.2f}')


# 2. Agrupar o total vendido por categoria
categorias = {
    categoria: sum(
        item["total"]
        for item in totais
        if item["categoria"] == categoria
    )
    for categoria in {item["categoria"] for item in totais}
}

print("\nTOTAIS POR CATEGORIA")
print("-" * 40)

for categoria, total in categorias.items():
    print(f"{categoria}: R$ {total:.2f}")


# 3. Produto mais vendido em valor total
mais_vendido = max(
    totais,
    key=lambda item: item["total"]
)

print("\nPRODUTO MAIS VENDIDO")
print("-" * 40)
print(f'Produto: {mais_vendido["produto"]}')
print(f'Total: R$ {mais_vendido["total"]:.2f}')