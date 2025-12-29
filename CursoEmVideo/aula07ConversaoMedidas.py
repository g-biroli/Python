# Conversor de medidas de Metros para outras medidas

medida = float(input('Digite a medida: '))
cm = medida * 100
mm = medida * 1000

print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))


