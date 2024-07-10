import csv

def carregar_dados(nome_arquivo):
    felinos = []
    file = open(nome_arquivo, mode='r', encoding='utf-8')
    reader = csv.DictReader(file)
    for row in reader:
        felinos.append(row)
    file.close()
    return felinos
def salvar_dados(nome_arquivo, felinos):
    file = open(nome_arquivo, mode='w', encoding='utf-8', newline='')
    fieldnames = felinos[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for felino in felinos:
        writer.writerow(felino)
    file.close()
def cadastrar_felino(felinos):
    novo_felino = {}
    novo_felino["Nome"] = input("Nome: ")
    novo_felino["Sexo"] = input("Sexo (M/F): ")
    novo_felino["Idade"] = input("Idade: ")
    novo_felino["Raça"] = input("Raça: ")
    novo_felino["Cor Predominante"] = input("Cor Predominante: ")
    novo_felino["Castrado"] = input("Castrado (Sim/Não): ")
    novo_felino["FIV+"] = input("FIV+ (Sim/Não): ")
    novo_felino["FELV+"] = input("FELV+ (Sim/Não): ")
    novo_felino["Data de Resgate"] = input("Data de Resgate (dd/mm/yyyy): ")
    novo_felino["Adotado"] = input("Adotado (Sim/Não): ")
    novo_felino["Lar Temporário"] = input("Lar Temporário (Sim/Não): ")
    novo_felino["Data de Adoção/Hospedagem"] = input("Data de Adoção/Hospedagem (dd/mm/yyyy): ")
    novo_felino["Tutor"] = input("Tutor: ")
    novo_felino["Contato"] = input("Contato: ")
    novo_felino["Data da Última Vacina"] = input("Data da Última Vacina (dd/mm/yyyy): ")
    novo_felino["Data da Última Desvermifugação"] = input("Data da Última Desvermifugação (dd/mm/yyyy): ")
    novo_felino["Data do Último Antipulgas"] = input("Data do Último Antipulgas (dd/mm/yyyy): ")
    novo_felino["Informações Extras"] = input("Informações Extras: ")
    felinos.append(novo_felino)
    print("Felino cadastrado com sucesso!")
def alterar_status_felino(felinos):
    for i, felino in enumerate(felinos):
        print(f"{i+1}. {felino['Nome']}")
    escolha = int(input("Escolha o número do felino que deseja alterar: ")) - 1
    
    felino = felinos[escolha]
    for key, value in felino.items():
        print(f"{key}: {value}")
    
    alterar = input("Digite o nome do campo que deseja alterar: ")
    novo_valor = input(f"Digite o novo valor para {alterar}: ")
    
    felino[alterar] = novo_valor
    print("Informação alterada com sucesso!")
def consultar_felino(felinos):
    for i, felino in enumerate(felinos):
        print(f"{i+1}. {felino['Nome']}")
    escolha = int(input("Escolha o número do felino que deseja consultar: ")) - 1
    
    felino = felinos[escolha]
    for key, value in felino.items():
        print(f"{key}: {value}")
def apresentar_estatisticas(felinos):
    total = len(felinos)
    machos = sum(1 for felino in felinos if felino["Sexo"] == "M")
    femeas = total - machos
    adotados = sum(1 for felino in felinos if felino["Adotado"].lower() == "sim")
    nao_adotados = total - adotados
    fiv_negativos = sum(1 for felino in felinos if felino["FIV+"].lower() == "não")
    felv_negativos = sum(1 for felino in felinos if felino["FELV+"].lower() == "não")
    fiv_positivos = total - fiv_negativos
    felv_positivos = total - felv_negativos
    
    print(f"Total de felinos: {total}")
    print(f"Machos: {machos} ({machos/total*100:.2f}%)")
    print(f"Fêmeas: {femeas} ({femeas/total*100:.2f}%)")
    print(f"Adotados: {adotados} ({adotados/total*100:.2f}%)")
    print(f"Não Adotados: {nao_adotados} ({nao_adotados/total*100:.2f}%)")
    print(f"Negativos para FIV+: {fiv_negativos} ({fiv_negativos/total*100:.2f}%)")
    print(f"Negativos para FELV+: {felv_negativos} ({felv_negativos/total*100:.2f}%)")
    print(f"Positivos para FIV+: {fiv_positivos} ({fiv_positivos/total*100:.2f}%)")
    print(f"Positivos para FELV+: {felv_positivos} ({felv_positivos/total*100:.2f}%)")
def filtrar_dados(felinos):
    print("1. Filtrar por período de resgate")
    print("2. Filtrar por período de adoção")
    escolha = int(input("Escolha uma opção: "))
    
    ano_inicio = int(input("Ano de início: "))
    ano_fim = int(input("Ano de fim: "))
    
    if escolha == 1:
        felinos_filtrados = [felino for felino in felinos if ano_inicio <= int(felino["Data de Resgate"].split('/')[-1]) <= ano_fim]
    elif escolha == 2:
        felinos_filtrados = [felino for felino in felinos if felino["Data de Adoção/Hospedagem"] and ano_inicio <= int(felino["Data de Adoção/Hospedagem"].split('/')[-1]) <= ano_fim]
    
    for felino in felinos_filtrados:
        print(f"{felino['Nome']}: Resgate em {felino['Data de Resgate']}, Adoção em {felino['Data de Adoção/Hospedagem']}")
def menu_principal(felinos, nome_arquivo):
    while True:
        print("\nMenu Principal")
        print("1. Cadastrar felino")
        print("2. Alterar status de felino")
        print("3. Consultar informações sobre felino")
        print("4. Apresentar estatísticas gerais")
        print("5. Filtragem de dados")
        print("6. Salvar")
        print("7. Sair do programa")
        
        escolha = int(input("Escolha uma opção: "))
        
        if escolha == 1:
            cadastrar_felino(felinos)
        elif escolha == 2:
            alterar_status_felino(felinos)
        elif escolha == 3:
            consultar_felino(felinos)
        elif escolha == 4:
            apresentar_estatisticas(felinos)
        elif escolha == 5:
            filtrar_dados(felinos)
        elif escolha == 6:
            salvar_dados(nome_arquivo, felinos)
            print("Dados salvos com sucesso!")
        elif escolha == 7:
            salvar_dados(nome_arquivo, felinos)
            print("Saindo do programa. Dados salvos com sucesso!")
            break
        else:
            print("Opção inválida. Tente novamente.")


nome_arquivo = 'felinos.csv'
felinos = carregar_dados(nome_arquivo)
menu_principal(felinos, nome_arquivo)
