situacao = None 

print('Helo, World!')
nome = input('Qual seu nome? ')

while situacao == None: # Enquanto a variável "situacao" for igual a None, o ciclo vai seguir indefinidamente.
    situacao = input(f'Olá, {nome}, como vai? [bem/mal]')
    if situacao == 'bem':
        print('Que bom! fico muito feliz!')
        break

    elif situacao == 'mal':
        print('Ah, não fique assim!! :(')
        break

    else:
        print('Não entendi oque disse :(')
        situacao = None #Toda vez que a variável "situacao" cair aqui, significa que não foi o esperado, então vai ser setada novamente para None.