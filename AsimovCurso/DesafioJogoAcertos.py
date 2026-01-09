respostas = {
    'Brasil': 'Brasilia',
    'Estados Unidos': 'Washington',
    'Inglaterra': 'Londres',
    'França': 'Paris',
    'Espanha': 'Madrid'
}

quer_continuar = True
rodadas = 0
acertos = 0
erros = 0

for pais, capital in respostas.items():
       
       if not quer_continuar:
            break
       rodadas +=1
       print(f'\n -> Qual a capital do pais {pais}? ')
       tentativa = input(f'Sua reposta: ')
       if tentativa.lower() == capital.lower():
            print(f'Parabéns, você acertou!')
            acertos +=1
       else:
            print(f'Infelizmente não era essa. A resposta correta era {capital}')
            erros +=1
        # Loop while para identificar se o usuario ainda quer jogar
       while True:
            opcao = input('Você deseja continuar? (s/n)').lower()
            if opcao == 's':
                  break
            elif opcao == 'n':
                quer_continuar = False
                break
            else:
                print('Responda apenas "S" para Sim ou "N" para não')
                  
porc = acertos / rodadas *100
print(f'Jogo finalizado, você conseguiu {acertos} acertos e {erros} erros. Você acertou {porc}%')        

