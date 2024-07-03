import csv

dados_felinos = [
    ["Nome", "Sexo", "Idade", "Raça", "Cor Predominante", "Castrado", "FIV+", "FELV+", "Data de Resgate", "Adotado", "Lar Temporário", "Data de Adoção/Hospedagem", "Tutor", "Contato", "Data da Última Vacina", "Data da Última Desvermifugação", "Data do Último Antipulgas", "Informações Extras"],
    ["Dudu", "M", 5, "SRD", "Amarelo", "Não", "Não", "Não", "12/01/2022", "Não", "Sim", "20/10/2022", "Felipe", "(51)5555-5555", "14/03/2024", "14/03/2024", "14/03/2024", ""],
    ["Fifi", "F", 36, "Siamês", "Creme", "Sim", "Não", "Sim", "29/05/2019", "Não", "Não", "", "", "", "09/12/2023", "09/12/2023", "14/03/2024", ""],
    ["Tuco", "M", 96, "SRD", "Preto", "Sim", "Não", "Sim", "04/09/2018", "Sim", "Não", "15/11/2021", "Rossana", "(51)5555-5555", "", "", "", "Rabinho cortado"],
    ["Xuga", "F", 88, "SRD", "Cinza", "Sim", "Sim", "Não", "10/12/2016", "Sim", "Não", "12/09/2017", "Janne", "(51)8888-8888", "", "", "", ""],
    ["Fiona", "F", 3, "Persa", "Branco", "Não", "", "", "14/03/2022", "Não", "Não", "", "", "", "05/12/2023", "05/12/2023", "05/12/2023", ""]
]

nome_arquivo = 'felinos.csv'

with open(nome_arquivo, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(dados_felinos)

print(f"Arquivo {nome_arquivo} criado com sucesso!")
