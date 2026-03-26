from modelscars import Vehicles
import json
from APIviaCEP import find_cep
import requests

database = []


def vehicle_register():
    tipo = input("Tipo (carro/moto): ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = input("Ano: ")
    cep = input("CEP: ")

    endereco = find_cep(cep)

    if endereco:
        v = Vehicles(tipo, marca, modelo, ano, cep, endereco)
        database.append(v.to_dict())
        print(" Veículo cadastrado com sucesso!")
    else:
        print("Erro ao cadastrar veículo.")


def vehicle_list():
    print("\n--- FROTA DE VEÍCULOS ---")

    if not database:
        print("Nenhum veículo cadastrado.")
        return

    for i, v in enumerate(database):
        print(f"\n{i}. {v['tipo'].upper()} - {v['marca']} {v['modelo']}")
        print(f"Ano: {v['ano']}")
        print(f"Local: {v['endereco']['localidade']} - {v['endereco']['uf']}")
        print(f"CEP: {v['cep']}")


def remove_vehicle():
    vehicle_list()
    idx = int(input("\nDigite o número do veículo para remover: "))

    if 0 <= idx < len(database):
        database.pop(idx)
        print("Veículo removido com sucesso!")
    else:
        print("Número inválido.")


def salvar():
    with open("veiculos.json", "w") as f:
        json.dump(database, f, indent=4)
    print("Banco salvo com sucesso!")


def carregar():
    global database
    try:
        with open("veiculos.json", "r") as f:
            database = json.load(f)
        print("Banco carregado com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado.")


    print("\n--- DEALERSHIP SYSTEM ---")
    print("1. Cadastrar Veículo")
    print("2. Listar Veículos")
    print("3. Remover Veículo")
    print("4. Salvar Dados")
    print("5. Carregar Dados")
    print("0. Sair")

    while True:
        opcao = input("Escolha: ")

        if opcao == "1":
         vehicle_register()

        elif opcao == "2":
         vehicle_list ()

        elif opcao == "3":
          remove_vehicle()

        elif opcao == "4":
          salvar()

        elif opcao == "5":
            carregar()

        elif opcao == "0":
         print("Encerrando sistema...")
        break