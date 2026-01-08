capitais = {
    'Brasil': 'Brasilia',
    'Espanha': 'Madrid',
    'Estados Unidos': 'Washighton',
    'Inglaterra': 'Londres',
    'França': 'Paris'
    }

pais = 'Alemanha'

if pais in capitais:
    capital = capitais[pais]
    print(f'O pais {pais} possui a capital {capital}')
else:
    print(f'Não há registros de capitais para o pais {pais}')

