# Classe de exceção personalizada
class CampoObrigatorioError(Exception):
    pass


def processar_registro(dado):

    try:
        # Verifica se a chave "nome" existe
        if "nome" not in dado:
            raise CampoObrigatorioError(
                "O campo 'nome' é obrigatório."
            )

        # Tenta converter idade para inteiro
        idade = int(dado["idade"])

    except ValueError:
        print("Erro: idade inválida.")

    except CampoObrigatorioError as erro:
        print("Erro:", erro)

    except KeyError:
        print("Erro: o campo 'idade' é obrigatório.")     

    else:
        print("Registro processado com sucesso.")
        print("Nome:", dado["nome"])
        print("Idade:", idade)

    finally:
        print("Processamento finalizado.")

# -----------------------------------------
# REGISTROS PARA TESTE
# -----------------------------------------

# Teste 1 - Registro válido
registro1 = {
    "nome": "João",
    "idade": "30"
}

# Teste 2 - Idade inválida
registro2 = {
    "nome": "Maria",
    "idade": "abc"
}

# Teste 3 - Sem nome
registro3 = {
    "idade": "25"
}

# Teste 4 - Sem idade
registro4 = {
    "nome": "Carlos"
}


print("\n--- TESTE 1 ---")
processar_registro(registro1)

print("\n--- TESTE 2 ---")
processar_registro(registro2)

print("\n--- TESTE 3 ---")
processar_registro(registro3)

print("\n--- TESTE 4 ---")
processar_registro(registro4)