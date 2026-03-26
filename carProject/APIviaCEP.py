import requests




def find_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    if response.status_code != 200:
        print("Erro ao consultar o CEP.")
        return None
    else:
        response = response.json()
        return f"Endereço encontrado: Rua: {response['logradouro']}, Bairro: {response['bairro']}, Cidade: {response['localidade']}, Estado: {response['uf']}"
