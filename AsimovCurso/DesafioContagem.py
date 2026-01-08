vogais = {
    'A': 0,
    'E': 0,
    'I': 0,
    'O': 0,
    'U': 0
}

texto = """
O Palmeiras foi até o estádio do Morumbi medir forças com o São Paulo em busca da liderança do Campeonato Brasileiro. A primeira etapa do clássico, no entanto, não foi positiva para o Verdão: 2 a 0 para o rival tricolor e a difícil missão de reverter o placar negativo. Porém, mais uma vez, o Maior Campeão do Brasil justificou a alcunha de “o time da virada”.

No segundo tempo, a equipe comandada pelo técnico Abel Ferreira voltou para fazer história. Aos 24 minutos, Vitor Roque anotou o primeiro tento palestrino e começou a reação na casa do São Paulo. Quatro minutos depois, foi a vez de Flaco López balançar as redes, e, aos 43, Ramón Sosa confirmou o que parecia impossível. Vitória épica por 3 a 2 e mais um embate inesquecível na história do Palmeiras.
"""
maiusculo = texto.upper()

for caracter in texto:
    if caracter.upper() == 'A':
        vogais['A'] += 1
    if caracter.upper() == 'E':
        vogais['E'] += 1
    if caracter.upper() == 'I':
        vogais['I'] += 1
    if caracter.upper() == 'O':
        vogais['O'] += 1
    if caracter.upper() == 'U':
        vogais['U'] += 1
    
for vogal, contagem in vogais.items():
    print(f'Há {contagem} letras {vogal} no texto')

