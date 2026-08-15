# Consultar CEP via API
import requests

cep = input("Informe o CEP: ")

# Remove hífen e espaços
cep = cep.replace("-", "").replace(" ", "")

# Validação básica
if not cep.isdigit() or len(cep) != 8:
    print("CEP inválido. Informe exatamente 8 números.")
else:
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url, timeout=10)

        resposta.raise_for_status()

        dados = resposta.json()

        if dados.get("erro"):
            print("CEP não encontrado.")
        else:
            print("\nENDEREÇO ENCONTRADO")
            print("-" * 40)
            print(f"CEP:         {dados.get('cep', '')}")
            print(f"Logradouro:  {dados.get('logradouro', '')}")
            print(f"Complemento: {dados.get('complemento', '')}")
            print(f"Bairro:      {dados.get('bairro', '')}")
            print(f"Cidade:      {dados.get('localidade', '')}")
            print(f"Estado:      {dados.get('uf', '')}")
            print("-" * 40)

    except requests.exceptions.Timeout:
        print("A consulta demorou demais. Tente novamente.")

    except requests.exceptions.ConnectionError:
        print("Não foi possível conectar à API. Verifique sua internet.")

    except requests.exceptions.RequestException as erro:
        print(f"Erro ao consultar o CEP: {erro}")