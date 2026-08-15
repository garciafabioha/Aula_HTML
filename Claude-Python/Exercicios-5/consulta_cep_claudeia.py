"""
Exercício 5 - Trabalhando com APIs (requisições HTTP)
Consulta de CEP usando a API pública ViaCEP.

- Recebe um CEP (ou vários, separados por vírgula) do usuário.
- Consulta https://viacep.com.br/ws/{cep}/json/
- Trata erros de conexão e CEP inválido/inexistente.
- Formata e imprime o endereço de forma legível.
- Bônus: aceita lista de CEPs e mostra o resultado em formato de tabela.
"""

import re
import sys
import requests

try:
    from tabulate import tabulate
    TABULATE_DISPONIVEL = True
except ImportError:
    TABULATE_DISPONIVEL = False

URL_VIACEP = "https://viacep.com.br/ws/{cep}/json/"
TIMEOUT_SEGUNDOS = 5


def limpar_cep(cep: str) -> str:
    """Remove tudo que não for dígito (pontos, traços, espaços)."""
    return re.sub(r"\D", "", cep)


def cep_valido(cep: str) -> bool:
    """Um CEP brasileiro válido (em formato) tem exatamente 8 dígitos."""
    return len(cep) == 8 and cep.isdigit()


def consultar_cep(cep: str) -> dict:
    """
    Consulta um único CEP na API ViaCEP.

    Retorna um dicionário sempre com a chave 'cep_consultado' e:
      - em caso de sucesso: os dados de endereço retornados pela API.
      - em caso de erro: a chave 'erro' com uma mensagem descritiva.
    """
    cep_limpo = limpar_cep(cep)

    if not cep_valido(cep_limpo):
        return {
            "cep_consultado": cep,
            "erro": "CEP inválido (deve conter 8 dígitos numéricos).",
        }

    try:
        resposta = requests.get(
            URL_VIACEP.format(cep=cep_limpo), timeout=TIMEOUT_SEGUNDOS
        )
        resposta.raise_for_status()
    except requests.exceptions.Timeout:
        return {
            "cep_consultado": cep,
            "erro": "Tempo de conexão esgotado ao consultar a API.",
        }
    except requests.exceptions.ConnectionError:
        return {
            "cep_consultado": cep,
            "erro": "Erro de conexão. Verifique sua internet e tente novamente.",
        }
    except requests.exceptions.HTTPError as e:
        return {
            "cep_consultado": cep,
            "erro": f"Erro HTTP ao consultar a API: {e}",
        }
    except requests.exceptions.RequestException as e:
        return {
            "cep_consultado": cep,
            "erro": f"Erro inesperado na requisição: {e}",
        }

    dados = resposta.json()

    # A API ViaCEP retorna {"erro": true} quando o CEP não existe.
    if dados.get("erro"):
        return {
            "cep_consultado": cep,
            "erro": "CEP não encontrado.",
        }

    dados["cep_consultado"] = cep
    return dados


def formatar_endereco(dados: dict) -> str:
    """Formata o dicionário de um CEP em texto legível para exibição."""
    if "erro" in dados:
        return f"CEP {dados['cep_consultado']}: ❌ {dados['erro']}"

    partes = [
        f"CEP:         {dados.get('cep', '-')}",
        f"Logradouro:  {dados.get('logradouro') or '-'}",
        f"Complemento: {dados.get('complemento') or '-'}",
        f"Bairro:      {dados.get('bairro') or '-'}",
        f"Cidade/UF:   {dados.get('localidade', '-')}/{dados.get('uf', '-')}",
    ]
    return "\n".join(partes)


def imprimir_tabela(resultados: list[dict]) -> None:
    """Imprime uma lista de resultados de CEP em formato de tabela."""
    linhas = []
    for dados in resultados:
        if "erro" in dados:
            linhas.append(
                [dados["cep_consultado"], "ERRO", dados["erro"], "-", "-", "-"]
            )
        else:
            linhas.append(
                [
                    dados.get("cep", dados["cep_consultado"]),
                    dados.get("logradouro") or "-",
                    dados.get("bairro") or "-",
                    dados.get("localidade") or "-",
                    dados.get("uf") or "-",
                    dados.get("complemento") or "-",
                ]
            )

    cabecalho = ["CEP", "Logradouro", "Bairro", "Cidade", "UF", "Complemento"]

    if TABULATE_DISPONIVEL:
        print(tabulate(linhas, headers=cabecalho, tablefmt="grid"))
    else:
        # Fallback simples caso a biblioteca 'tabulate' não esteja instalada.
        largura = [len(c) for c in cabecalho]
        for linha in linhas:
            for i, valor in enumerate(linha):
                largura[i] = max(largura[i], len(str(valor)))

        def imprimir_linha(colunas):
            print(
                " | ".join(
                    str(c).ljust(largura[i]) for i, c in enumerate(colunas)
                )
            )

        imprimir_linha(cabecalho)
        print("-+-".join("-" * w for w in largura))
        for linha in linhas:
            imprimir_linha(linha)


def main():
    print("=== Consulta de CEP (ViaCEP) ===")
    entrada = input(
        "Digite um CEP ou vários separados por vírgula (ex: 01310-100, 20040-020): "
    ).strip()

    if not entrada:
        print("Nenhum CEP informado. Encerrando.")
        sys.exit(1)

    ceps = [c.strip() for c in entrada.split(",") if c.strip()]

    resultados = [consultar_cep(cep) for cep in ceps]

    if len(resultados) == 1:
        print("\n" + formatar_endereco(resultados[0]))
    else:
        print()
        imprimir_tabela(resultados)


if __name__ == "__main__":
    main()