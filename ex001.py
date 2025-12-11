''' Pedro tem muitas notas de 2 e de 5 reais. Ele precisa pagar uma conta de 20 reais. De quantas maneiras diferentes Pedro pode pagar essa conta sem receber troco?'''
#Feito pelo gemini
def contar_maneiras_pagar(valor_total, nota1, nota2):
    """
    Calcula o número de maneiras de pagar um valor_total usando 
    apenas duas denominações de notas (nota1 e nota2), sem troco.
    """
    
    # Define as notas para facilitar a iteração pela maior
    notas = sorted([nota1, nota2], reverse=True)
    nota_maior = notas[0]  # R$ 5
    nota_menor = notas[1]  # R$ 2
    
    # O número máximo de notas maiores que podemos usar é o valor_total / nota_maior
    max_maior = valor_total // nota_maior
    
    contador = 0
    # Itera sobre todas as possibilidades de notas maiores (R$ 5)
    for num_maior in range(max_maior + 1):
        # Calcula o valor pago pelas notas maiores
        valor_pago_maior = num_maior * nota_maior
        
        # Calcula o valor restante a ser pago pelas notas menores (R$ 2)
        valor_restante = valor_total - valor_pago_maior
        
        # Verifica se o restante é divisível pela nota menor.
        # Se for, significa que encontramos uma combinação válida.
        if valor_restante >= 0 and valor_restante % nota_menor == 0:
            # O número de notas menores seria: valor_restante / nota_menor
            num_menor = valor_restante // nota_menor
            
            # Imprime ou armazena a combinação encontrada (opcional)
            print(f"Combinação Válida: {num_menor} notas de R${nota_menor},00 e {num_maior} notas de R${nota_maior},00.")
            contador += 1
            
    return contador

# Parâmetros do problema
valor_total = 50
nota_2 = 2
nota_5 = 5

resultado = contar_maneiras_pagar(valor_total, nota_2, nota_5)

print(f"\nNúmero total de maneiras: {resultado}")