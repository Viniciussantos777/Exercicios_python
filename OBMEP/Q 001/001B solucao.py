''' Pedro tem muitas notas de 2 e de 5 reais. Ele precisa pagar uma conta de 20 reais. De quantas maneiras diferentes Pedro pode pagar essa conta sem receber troco?'''
# Feito por mim

def maneiras_de_pagar(valor_maximo, nota1, nota2):

    possibilidades = []
    for valor in range(valor_maximo, 0, -1):
        
        if nota1*valor == valor_maximo:
            possibilidades.append(valor)
        
        if nota2*valor == valor_maximo:
            possibilidades.append(valor)
            
    for valor in range(valor_maximo, 0, -1):
        for valor2 in range(valor_maximo, 0, -1):
            if nota1*valor+nota2*valor2 == valor_maximo:
                possibilidades.append(20)
        
        
    print(f'Com as notas de R${nota1},00 e R${nota2},00 existem {len(possibilidades)} possibilidades de combinação.')
    
print(maneiras_de_pagar(20,2,5))
