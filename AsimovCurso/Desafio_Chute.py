numero_secreto = 33
descobriu = False

for n in range(3):
    if not descobriu:
        chute = int(input("Acerte o número secreto! \nChute um número: "))
        print(chute)
        if chute > numero_secreto:
            print('O seu palpite foi maior que o número secreto, tente novamente :)')
        elif chute < numero_secreto:
            print('Seu palpite foi menor que o número secreto, tente novamente :)')
        else:
            print('Descobriu!')
            descobriu = True

if descobriu:
    print('Parábens você ganhou 1 milhão de reais!')
else:
    print(f'Infelizmente não foi dessa vez. \nO número secreto era {numero_secreto}')