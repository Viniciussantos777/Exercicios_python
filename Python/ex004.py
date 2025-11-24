num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o último número: '))

for pares in range(num1, num2):
    if pares % 2 == 0:
        print(pares)
print('FIM')