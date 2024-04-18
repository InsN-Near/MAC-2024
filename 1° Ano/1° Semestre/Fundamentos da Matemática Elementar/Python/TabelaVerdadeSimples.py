import tkinter as tk
from tkinter import ttk

def gerar_tabela_verdade(n):
    """
    Gera os dados da tabela-verdade para n proposições.
    """
    data = []
    for i in range(2**n):
        linha = []
        for j in range(n):
            # Calcula o padrão de V/F para cada proposição
            linha.append("V" if (i // 2**j) % 2 == 0 else "F")
        data.append(linha)
    return data

def criar_interface(n):
    """
    Cria a interface gráfica para a tabela-verdade com rolagem.
    """
    root = tk.Tk()
    root.title("Gerador de Tabela-Verdade")

    # Frame para a tabela com barra de rolagem
    tabela_frame = tk.Frame(root)
    tabela_frame.pack()

    # Criar canvas e barra de rolagem vertical
    canvas = tk.Canvas(tabela_frame)
    scrollbar = ttk.Scrollbar(tabela_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Criar um frame interno para a tabela
    inner_frame = tk.Frame(canvas)

    # Cabeçalho da tabela
    for i in range(n):
        tk.Label(inner_frame, text=f"P{i+1}", borderwidth=1, relief="solid").grid(row=0, column=i)

    # Gerar dados da tabela
    data = gerar_tabela_verdade(n)

    # Criar células da tabela no frame interno
    for i, linha in enumerate(data):
        for j, valor in enumerate(linha):
            tk.Label(inner_frame, text=valor, borderwidth=1, relief="solid").grid(row=i+1, column=j)

    # Adicionar o frame interno ao canvas
    canvas.create_window((0, 0), window=inner_frame, anchor='nw')
    canvas.update_idletasks()  # Atualizar o canvas para obter as dimensões corretas

    # Configurar a região de rolagem do canvas
    canvas.configure(scrollregion=canvas.bbox("all"))

    # Posicionar o canvas e a barra de rolagem
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Botão para gerar nova tabela
    tk.Button(root, text="Gerar Nova Tabela", command=lambda: nova_tabela(root)).pack()

    root.mainloop()

def nova_tabela(root):
    """
    Fecha a janela atual e pede ao usuário um novo número de proposições.
    """
    # Fecha a janela atual
    root.destroy()

    # Obtém o novo número de proposições
    novo_n = int(input("Digite o número de proposições: "))

    # Cria uma nova interface com o novo número de proposições
    criar_interface(novo_n)

if __name__ == "__main__":
    n = int(input("Digite o número de proposições: "))
    criar_interface(n)