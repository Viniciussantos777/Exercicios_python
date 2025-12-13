from collections import Counter

jabuti = Counter('JABUTI')
cabra = Counter('CABRA')
jabuticaba = Counter('JABUTICABA')

total = {
    'JABUTI': 40,
    'CABRA': 19,
    'JABUTICABA': 55
}

valor_caba = total['JABUTICABA'] - total['JABUTI']

R = total['CABRA'] - valor_caba

print('Valor da letra R:', R)

