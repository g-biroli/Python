#Desafio de valores duplicados
lista_jogadores1 = ['Neymar', 'Gabriel Jesus', 'Endrick', 'Estevão', 'Raphael Veiga']
lista_jogadores2 = ['Ronaldo', 'Ronaldinho', 'Endrick', 'Raphael Veiga', 'Romário']

#Utilização do loop For para toda vez 'para' toda vez que lista1 (Variavel criada) estiver dentro da lista criada e por tanto ja verificar a variavel 2 na lista 2 =, então parte para a condição if
for lista1 in lista_jogadores1:
    for lista2 in lista_jogadores2:
        if lista1 == lista2:
            print(f'Os jogadores duplicados são: {lista1}')