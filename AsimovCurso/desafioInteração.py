# Criação de uma lista
valores = [10, 30, -8, 0, -2, 4]

# Lógica da soma sem usar as funções matemáticas
soma = 0
for valor in valores:
    soma += valor

print(f'A soma dos valores {valores} é: {soma}!')

#Mesmo resultado, porém com a função Sum
print(sum(valores))

#Média dos elementos sem a função average
media = soma / len(valores)

print(f'A média dos Elementos {valores} é {media}')
print('\n\n\n\n')

#----------------------------------#
#Descobrindo o valor Máximo sem formula Max()
valores = [10, 30, -8, 0, -2, 4]

maximo = valores[0]

for valor in valores:
    if valor > maximo:
        maximo = valor

print(f'O valor máximo é: {maximo}')
