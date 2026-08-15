"""
Exercício 6 - Totais de vendas por produto, por categoria e produto mais vendido.

Dada uma lista de vendas (produto, categoria, valor unitário e quantidade),
calcula:
  1. O total (valor * qtd) de cada venda.
  2. O total vendido por categoria.
  3. O produto mais vendido em valor total.
"""

from collections import defaultdict


vendas = [
    {"produto": "Caneta", "categoria": "Papelaria", "valor": 2.5, "qtd": 10},
    {"produto": "Caderno", "categoria": "Papelaria", "valor": 15.0, "qtd": 3},
    {"produto": "Mouse", "categoria": "Eletrônicos", "valor": 45.0, "qtd": 2},
]


def calcular_totais(vendas: list[dict]) -> list[dict]:
    """Calcula o total (valor * qtd) de cada venda, mantendo produto e categoria."""
    return [
        {
            "produto": venda["produto"],
            "categoria": venda["categoria"],
            "total": venda["valor"] * venda["qtd"],
        }
        for venda in vendas
    ]


def agrupar_por_categoria(totais: list[dict]) -> dict:
    """
    Agrupa o total vendido por categoria em uma única passada.
    Usa defaultdict para não precisar checar se a chave já existe,
    e preserva a ordem em que cada categoria apareceu primeiro.
    """
    categorias = defaultdict(float)
    for item in totais:
        categorias[item["categoria"]] += item["total"]
    return dict(categorias)


def produto_mais_vendido(totais: list[dict]) -> dict | None:
    """Retorna o item (produto) com maior total vendido, ou None se a lista estiver vazia."""
    if not totais:
        return None
    return max(totais, key=lambda item: item["total"])


def imprimir_secao(titulo: str) -> None:
    print(f"\n{titulo.upper()}")
    print("-" * 40)


def main():
    if not vendas:
        print("Nenhuma venda registrada.")
        return

    totais = calcular_totais(vendas)

    imprimir_secao("Totais por produto")
    for item in totais:
        print(f'{item["produto"]}: R$ {item["total"]:.2f}')

    categorias = agrupar_por_categoria(totais)
    imprimir_secao("Totais por categoria")
    for categoria, total in categorias.items():
        print(f"{categoria}: R$ {total:.2f}")

    melhor = produto_mais_vendido(totais)
    imprimir_secao("Produto mais vendido")
    print(f'Produto: {melhor["produto"]}')
    print(f'Total: R$ {melhor["total"]:.2f}')


if __name__ == "__main__":
    main()