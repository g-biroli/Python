respostas = {
    'Brasil': 'Brasilia',
    'Estados Unidos': 'Washington',
    'Inglaterra': 'Londres',
    'França': 'Paris',
    'Espanha': 'Madrid'
}

for pais, capital in respostas:
    print(f'\n -> Qual a capital do pais {pais}? ')
    tentativa = input(f'Sua reposta: ')