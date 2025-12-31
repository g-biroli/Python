#Desafio de programa de Entrevista

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))
tamanho_nome = str(len(nome))
idade_futura = idade + 5

# Utilização da F STRING para digitar e formar frases é mais prático e deixa o código mais simples.
# É possivel colocar variaveis apenas usando os colchetes {}, também é possivel fazer operações matematicas e operações do propria python, como tamanho do texto, colocar letras maiusculas.
print(f'Prazer {nome} eu sou o Gabriel, analista de dados da Mercedez, como posso te ajudar?')
print(f'Seu nome possui {tamanho_nome} letras')
print(f'Interessante saber que você tem {idade} eu tenho uma idade um pouco mais abaixo, tenho 25 anos, daqui a 5 anos você terá {idade_futura} anos.')
