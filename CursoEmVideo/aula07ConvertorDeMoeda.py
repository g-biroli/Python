# Conversor de real para outras moedas

real = float(input('Quanto dinheiro você tem na carteira? '))
dolar = real / 5.67
euro = real / 6.14
peso = real / 0.0058
libra = real / 7.37

print('Com R${} você pode comprar U${}'.format(real, dolar))
print('Com R${} você pode compra €{}'.format(real, euro))
print('Com R${} você pode comprar £{}'.format(real, libra))
print('Com R${} você pode comprar ARS${}'.format(real, peso))



