lista_candidatos = {}

while True:
    print(f'digite os dados do candidato (ou digite sair para encerrar)')
    nome = input('nome do candidato: ')
    if nome.lower() == 'sair':
        break

    cod = input('digite o numero de dois digitos do candidato: ')

    if cod.isdigit():
        cod = int(cod)
        lista_candidatos[nome] = cod
    else:
        print('código inválido:')

    print('candidato adicionado!')

print(f'candidatos cadastrados: ')
for nome, cod in lista_candidatos.items():
    
    print(f'nome: {nome}, codigo: {cod}')