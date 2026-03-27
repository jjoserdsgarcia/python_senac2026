import requests

def find_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)

    if response.status_code != 200:
        print("Erro ao consultar o CEP.")
        return None

    dados = response.json()

    if "erro" in dados:
        print("CEP não encontrado.")
        return None

    return dados  
