import tkinter as tk

def calcular_aumento():
    preco = float(entry_preco.get())
    aumento = 5/100
    novo_preco = preco + (preco * aumento)
    label_resultado['text'] = f'O preço com aumento de 5% é de R${novo_preco:.2f}'

# Cria a janela principal
janela = tk.Tk()
janela.title('Calculadora de Aumento de Preço')

# Cria os componentes da interface
label_preco = tk.Label(janela, text='Qual o valor do produto?')
label_preco.pack()

entry_preco = tk.Entry(janela)
entry_preco.pack()

button_calcular = tk.Button(janela, text='Calcular', command=calcular_aumento)
button_calcular.pack()

label_resultado = tk.Label(janela)
label_resultado.pack()

# Inicia o loop da interface gráfica
janela.mainloop()
