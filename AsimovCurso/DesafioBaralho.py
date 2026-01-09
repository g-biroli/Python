import random

# Função para gerar baralho
def gerar_baralho (n_copias=2, coringa=True, embaralhado=True):
    #Função for para agregar carta com naipe e gerar o baralho
    #Criação da variavel para resultado final do baralho
    novo_baralho = []
    naipes = list('♠♥♦♣')
    cartas = list('A23456789') + ['10'] + list('JQK')

    for _ in range(n_copias):
        for naipe in naipes:
            for carta in cartas:
                carta_especifica = carta + naipe
                novo_baralho.append(carta_especifica)
            if coringa:
                novo_baralho.append(['JK1', 'JK2'])
            if embaralhado:
                random.shuffle(novo_baralho)
            
            return novo_baralho
    
def mostrar_baralho(novo_baralho):
    print(f'Há {len(novo_baralho)} cartas no baralho')
    print('Cartas:')
    print(' | '.join(novo_baralho))

def dar_as_cartas(novo_baralho, n_cartas = 4, n_jogadores = 5):
    jogadores = {}
    for i in range(n_jogadores):
        mao = []
        while (len(mao)) < n_cartas:
            carta = novo_baralho.pop()
            mao.append(carta)
        nome_jogadores = f'Jogador {i+1}'
        jogadores[nome_jogadores] = mao
        return jogadores

def mostrar_jogadores(jogadores):
    for jogadores, mao in jogadores.items():
        print(f'Há {len(mao)} cartas na mão do jogador {jogadores}')
        print('Cartas:')
        for carta in mao:
            print(f'-> {carta}')


novo_baralho = gerar_baralho()
print(novo_baralho)
jogadores = dar_as_cartas(novo_baralho)
print(jogadores)
