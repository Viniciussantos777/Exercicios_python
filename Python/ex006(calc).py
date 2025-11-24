from time import sleep
def somar(a, b):
    resultado_som = a + b
    return resultado_som

def subtrair(a, b):
    resultado_sub = a - b
    return resultado_sub

def multiplicar(a, b):
    resultado_mult = a * b
    return resultado_mult

def dividir(a, b):
    resultado_div = a / b
    return resultado_div

def resto(a, b):
    resultado_resto = a % b
    return resultado_resto


while 1 == 1:
    print('-='*20)
    print('Calculadora do Vini')
    print('Escolha uma opção:')
    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Resto')
    print('Digite EXIT para sair do programa!')
    print('-='*20)

    resposta1 = input('Digite sua escolha: ').upper()

    try:
        if resposta1 == 'EXIT':
            print('Saindo do programa!')
            sleep(1)
            break

        else:
            

            if resposta1 == '1':
                a = float(input('Digite o primeiro número: '))

                b = float(input('Digite o segundo número: '))
                print(f'A soma entre {a} e {b} é igual a: {somar(a,b)}')
                sleep(1)

            elif resposta1 == '2':
                a = float(input('Digite o primeiro número: '))

                b = float(input('Digite o segundo número: '))
                print(f'A subtração entre {a} e {b} é igual a: {subtrair(a,b)}')
                sleep(1)

            elif resposta1 == '3':
                a = float(input('Digite o primeiro número: '))

                b = float(input('Digite o segundo número: '))
                print(f'A multiplicação entre {a} e {b} é igual a: {multiplicar(a,b)}')
                sleep(1)

            elif resposta1 == '4':
                a = float(input('Digite o primeiro número: '))

                b = float(input('Digite o segundo número: '))
                if b == 0:
                    print('Não existe divisão por 0!')
                else:
                    print(f'A divisão entre {a} e {b} é igual a: {dividir(a,b)}')
                sleep(1)

            elif resposta1 == '5':
                a = float(input('Digite o primeiro número: '))

                b = float(input('Digite o segundo número: '))
                if b == 0:
                    print('Não existe divisão por 0!')
                else:
                    print(f'O resto da divisão entre {a} e {b} é igual a: {resto(a,b)}')
                sleep(1)

    except ValueError:
        print('Digite apenas oque está nas opções ou oque for pedido!')
        sleep(1)