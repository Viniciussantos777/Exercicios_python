import tkinter as tk

expressao = ''

def clicar_numero(numero):
    #Adiciona o número ou operador à expressão e atualiza o display.
    global expressao
    expressao = expressao + str(numero)
    campo_texto.delete(0, tk.END)
    campo_texto.insert(0,expressao)

def limpar():
    #Apagar toda a conta (Clear All). Limpa a variável expressao e o display.
    global expressao
    expressao = ''
    campo_texto.delete(0,tk.END)

def backspace():
    #Apagar a expressão (DEL). Remove o último caractere da string expressao.
    global expressao
    # retorna a string sem o último caractere
    expressao = expressao[:-1] 
    campo_texto.delete(0, tk.END)
    campo_texto.insert(0, expressao)

def calcular():
    #Avalia a expressão e exibe o resultado.
    global expressao
    try:
        # Usa eval() para calcular o resultado da string expressao
        resultado = str(eval(expressao))
        campo_texto.delete(0,tk.END)
        campo_texto.insert(0,resultado)
        expressao = resultado
    except:
        campo_texto.delete(0,tk.END)
        campo_texto.insert(0,"ERRO")
        expressao = ''

janela = tk.Tk()
janela.title('Calculadora')
janela.geometry('280x300')

campo_texto = tk.Entry(janela, width=20, borderwidth=5, font=('Arial',16), justify='right')
campo_texto.grid(row=0,column=0,columnspan=4,padx=10,pady=10)



# Botão 'C' - Chama limpar() para apagar toda a conta
button_clear = tk.Button(janela, text = 'C', padx = 10, pady = 10, font=('Arial',10), command=limpar)
button_clear.grid(row=1, column=0, columnspan=2, sticky='we') 

# Botão 'DEL' - Chama backspace() para apagar o último dígito
button_del = tk.Button(janela, text = 'DEL', padx = 10, pady = 10, font=('Arial',10), command=backspace)
button_del.grid(row=1, column=2, columnspan=2, sticky='we') 

# --- LINHAS DE NÚMEROS E OPERAÇÕES (ROW 2 a 5) ---

# Coluna 0
button_7 = tk.Button(janela, text = 7, padx = 10, pady = 10, font=('Arial',10), command=lambda: clicar_numero(7))
button_4 = tk.Button(janela, text = 4, padx = 10, pady = 10, font=('Arial',10), command=lambda: clicar_numero(4))
button_1 = tk.Button(janela, text = 1, padx = 10, pady = 10, font=('Arial',10), command=lambda: clicar_numero(1))
button_0 = tk.Button(janela, text = 0, padx = 10, pady = 10, font=('Arial',10), command=lambda: clicar_numero(0))

button_7.grid(row=2, column=0)
button_4.grid(row=3, column=0)
button_1.grid(row=4, column=0)
button_0.grid(row=5, column=0)

# Coluna 1
button_8 = tk.Button(janela, text = 8, padx = 10, pady = 10, font=('Arial',10), command=lambda: clicar_numero(8))
button_5 = tk.Button(janela, text = 5, padx = 10, pady = 10, font=('Arial',10), command=lambda: clicar_numero(5))
button_2 = tk.Button(janela, text = 2, padx = 10, pady = 10, font=('Arial',10), command=lambda: clicar_numero(2))
button_dot = tk.Button(janela, text = '.', padx = 11.49, pady = 10, font=('Arial',10), command=lambda: clicar_numero('.'))

button_8.grid(row=2, column=1)
button_5.grid(row=3, column=1)
button_2.grid(row=4, column=1)
button_dot.grid(row=5, column=1)

# Coluna 2
button_9 = tk.Button(janela, text = 9, padx = 10, pady = 10, font=('Arial',10), command=lambda: clicar_numero(9))
button_6 = tk.Button(janela, text = 6, padx = 10, pady = 10, font=('Arial',10), command=lambda: clicar_numero(6))
button_3 = tk.Button(janela, text = 3, padx = 10, pady = 10, font=('Arial',10), command=lambda: clicar_numero(3))

button_igual = tk.Button(janela, text = '=', padx = 10, pady = 10, font=('Arial',10), command=calcular) 

button_9.grid(row=2, column=2)
button_6.grid(row=3, column=2)
button_3.grid(row=4, column=2)
button_igual.grid(row=5, column=2)

# Coluna 3
button_add = tk.Button(janela, text = '+', padx = 8.5, pady = 10, font=('Arial',10), command=lambda: clicar_numero('+'))
button_sub = tk.Button(janela, text = '-', padx = 10, pady = 10, font=('Arial',10), command=lambda: clicar_numero('-'))
button_div = tk.Button(janela, text = '/', padx = 10, pady = 10, font=('Arial',10), command=lambda: clicar_numero('/'))
button_mult = tk.Button(janela, text = '*', padx = 10, pady = 10, font=('Arial',10), command=lambda: clicar_numero('*'))

button_add.grid(row=2, column=3)
button_sub.grid(row=3, column=3)
button_div.grid(row=4, column=3)
button_mult.grid(row=5, column=3)

janela.mainloop()