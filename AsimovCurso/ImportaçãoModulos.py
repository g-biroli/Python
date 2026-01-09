import random

nomes = ['gabriel', 'ana', 'luigi', 'julia', 'davi', 'mirela', 'cristina', 'beto', 'thiago', 'mariana']
for n in range(2):
    n = random.choice(nomes)
    print(f'O casal feito foi: {n}')