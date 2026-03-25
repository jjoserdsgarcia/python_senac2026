import json

database = []

def abrir_chamado(laboratorio, descricao, prioridade):

    if prioridade < 1 or prioridade > 10: 
        print("Erro: A prioridade deve ser entre 1 e 10.")
        return False

    chamado = {
        "lab": laboratorio,
        "descricao": descricao,
        "prioridade": prioridade,
        "status": "Aberto"
    }
    database.append(chamado)
    print(" Chamado registrado com sucesso!")

    return True

while True:
    print("\n--- HELP DESK TÉCNICO ---")
    print("1. Novo Chamado")
    print("2. Listar Chamados")
    print("3. Fechar Chamado")
    print("4. Listar Chamados de Alta Prioridade")
    print("5. Salvar o Banco de Dados")
    print("6. Carregar o Banco de Dados")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        l = input("Laboratório: ")
        d = input("Descrição do problema: ")
        p = int(input("Prioridade (1-10): "))
        abrir_chamado(l, d, p)

    elif opcao == "2":
        print("\n--- TODOS OS CHAMADOS ---")
        for c in database:
            print(f"[{c['status']}] Lab: {c['lab']} - {c['descricao']} (Prioridade: {c['prioridade']})")
           
    
    elif opcao == "3":
        print("\n--- FECHAR CHAMADO ---")
        for i, c in enumerate(database):
            print(f"{i}. [{c['status']}] Lab: {c['lab']} - {c['descricao']} (Prioridade: {c['prioridade']})")
        idx = int(input("Digite o número do chamado para fechar: "))
        if 0 <= idx < len(database):
            database[idx]['status'] = "Fechado"
            print("Chamado fechado com sucesso!")
        else:
            print("Número de chamado inválido.")
            
        
    elif opcao == "4":
        print ("\n--- Chamados de Alta Prioridade (8-10) ---")
        encontrou = False
        for c in database:
            if c['prioridade'] >= 8:
                print(f"[{c['status']}] Lab: {c['lab']} - {c['descricao']} (Prioridade: {c['prioridade']})")
                encontrou = True

        if not encontrou:
            print("Nenhum chamado de alta prioridade encontrado.")

    elif opcao == "5":
        
        with open("chamados.json", "w") as file:
            json.dump(database, file, indent=4)
        print("Banco de dados salvo com sucesso!")

    elif opcao == "6":
        
        try:
            with open("chamados.json", "r") as file:
                database = json.load(file)
            print("Banco de dados carregado com sucesso!")
        except FileNotFoundError:
            print("Arquivo de banco de dados não encontrado. Iniciando com um banco vazio.")

    elif opcao == "0":
        print("Desligando sistema...")
        break