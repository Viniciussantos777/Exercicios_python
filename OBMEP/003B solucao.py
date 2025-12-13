import itertools

bolas = [1,2,3,4,5]
pesos = [1.0, 0.5]

for combinacao in itertools.product(pesos, repeat=5):
    if combinacao.count(0.5) != 2:
        continue
    
    bola1,bola2,bola3,bola4,bola5 = combinacao
    
    if bola1 + bola2 + bola3 != bola4 + bola5:
        continue
    
    if bola2 + bola5 <= bola1 + bola4:
        continue
    
    print('Combinação:')
    for i,peso in enumerate(combinacao,start=1):
        print(f'Bola {i}: {peso} kg')
        