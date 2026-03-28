from modelscars import Vehicles
import json
from APIviaCEP import find_cep
import requests

database = []


def vehicle_register():
    print("\n--- REGISTER VEHICLE ---")
    
    name = input("Owner's Name: ")
    type = input("Vehicle Type: ")
    brand = input("Brand: ")
    release_year = int(input("Release Year: "))
    cep = input("CEP: ")
    endereco = find_cep(cep)
    if endereco is None:
        print("Não foi possível encontrar o endereço para o CEP fornecido.")
        return

    vehicle = Vehicles(name, type, brand, release_year, cep, endereco)
    database.append(vehicle.to_dict())
    print("Veículo cadastrado com sucesso!")
    return True


def vehicle_list():
    print("\n--- VEHICLE LIST ---")

    if not database:
        print("Nenhum veículo cadastrado.")
        return

    for i, v in enumerate(database):
        print(f"\n{i}. {v['name']} - {v['type']} - {v['brand']} ({v['release_year']})")
        print(f"CEP: {v['cep']}")
        print(f"Cidade: {v['endereco']['localidade']} - {v['endereco']['uf']}")

def remove_vehicle():
    print("\n--- REMOVE VEHICLE ---")
    vehicle_list()
    idx = int(input("Digite o número do veículo para remover: "))
    if 0 <= idx < len(database):
        removed_vehicle = database.pop(idx)
        print(f"Veículo de '{removed_vehicle['name']}' removido com sucesso!")
    else:
        print("Número de veículo inválido.")

def salvar():
    with open("vehicles.json", "w") as f:
        json.dump(database, f, indent=4)
    print("Dados salvos com sucesso!")


def carregar():
    global database
    try:
        with open("vehicles.json", "r") as f:
            database = json.load(f)
        print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print("Nenhum arquivo de dados encontrado. Iniciando com um banco de dados vazio.")

def search_by_cep():
    cep_busca = input("Digite o CEP: ")

    encontrados = [v for v in database if v['cep'] == cep_busca]

    if encontrados:
        for v in encontrados:
            print(f"{v['name']} - {v['brand']} ({v['release_year']})")
    else:
        print("Nenhum veículo encontrado.")





while True:
    print("\n--- DEALERSHIP SYSTEM ---")
    print("1. Cadastrar Veículo")
    print("2. Listar Veículos")
    print("3. Remover Veículo")
    print("4. Salvar Dados")
    print("5. Carregar Dados")
    print("6. Buscar CEP")
    print("0. Sair")

    while True:
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            vehicle_register()
            break
        elif opcao == "2":
            vehicle_list()
            break
        elif opcao == "3":
            remove_vehicle()
            break
        elif opcao == "4":
            salvar()
            break
        elif opcao == "5":
            carregar()
            break
        elif opcao == "6":
            search_by_cep()
            break
        elif opcao == "0":
            print("Saindo do sistema. Até logo!")
            exit()
        else:
            print("Opção inválida. Por favor, tente novamente.")