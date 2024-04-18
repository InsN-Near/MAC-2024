import tkinter as tk

def calcular_determinante():
    try:
        n = int(entry_ordem.get())
        elementos_str = entry_elementos.get().split()
        elementos = [float(x) for x in elementos_str]

        if len(elementos) != n * n:
            raise ValueError("Número incorreto de elementos para a ordem da matriz.")

        # Constrói a matriz a partir da lista de elementos
        matriz = [elementos[i:i+n] for i in range(0, len(elementos), n)]

        determinante_valor = determinante(matriz)
        resultado_label.config(text=f"O determinante da matriz é: {determinante_valor}")
    except ValueError as e:
        resultado_label.config(text=f"Erro: {e}")

def determinante(matriz):
    n = len(matriz)

    '''A função determinante() é implementada de forma recursiva para calcular o determinante
      de uma matriz. Ela utiliza a expansão do determinante pela primeira linha da matriz, 
      calculando o cofator de cada elemento e somando-os para obter o valor do determinante.'''

    # Caso base: matriz 1x1
    if n == 1:
        return matriz[0][0]

    # Caso recursivo: expande o determinante pela primeira linha
    determinante_valor = 0
    for j in range(n):
        # Cria a submatriz excluindo a primeira linha e a j-ésima coluna
        submatriz = [linha[:j] + linha[j+1:] for linha in matriz[1:]]
        # Calcula o cofator
        cofator = (-1) ** j * matriz[0][j] * determinante(submatriz)
        determinante_valor += cofator

    return determinante_valor

# Interface gráfica
janela = tk.Tk()
janela.title("Calculadora de Determinante")

ordem_label = tk.Label(janela, text="Ordem da matriz (n):")
ordem_label.pack()

entry_ordem = tk.Entry(janela)
entry_ordem.pack()

elementos_label = tk.Label(janela, text="Elementos da matriz (a_ij):")
elementos_label.pack()

entry_elementos = tk.Entry(janela, width=50)
entry_elementos.pack()

calcular_button = tk.Button(janela, text="Calcular Determinante", command=calcular_determinante)
calcular_button.pack()

resultado_label = tk.Label(janela, text="")
resultado_label.pack()

janela.mainloop()