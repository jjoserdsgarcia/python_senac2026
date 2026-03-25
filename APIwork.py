import requests


cep = input(f"Qual o CEP? ")
response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
if response.status_code != 200:
    print("Erro ao consultar o CEP.")
else:
    resposta = response.json()
    print(f"Endereço encontrado: Rua: {resposta['logradouro']}, Bairro: {resposta['bairro']}, Cidade: {resposta['localidade']}, Estado: {resposta['uf']}")
