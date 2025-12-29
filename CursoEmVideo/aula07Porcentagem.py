# Calculo de porcentagem -> Desconto de loja 5%

preço = float(input('Qual é o preço do produto? R$'))

#novo = novo preco
novo = preço - (preço * 5 / 100)

print('O produto que custava R${} com o desconto de 5%, agora custa R${}'.format(preço, novo))

