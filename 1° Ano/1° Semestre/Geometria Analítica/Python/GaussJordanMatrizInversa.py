from fractions import Fraction

def inversa_gauss_jordan(matriz):
    """
    Calcula a inversa de uma matriz quadrada usando o método de Gauss-Jordan e exibe os resultados como frações.

    Args:
        matriz: Uma lista de listas representando uma matriz quadrada.

    Returns:
        Uma lista de listas representando a matriz inversa, ou None se a matriz não for invertível.
    """

    n = len(matriz)
    matriz_aumentada = [linha[:] + [1 if j == i else 0 for j in range(n)] for i, linha in enumerate(matriz)]

    for i in range(n):
        # Pivoteamento parcial (se necessário)
        if matriz_aumentada[i][i] == 0:
            for j in range(i + 1, n):
                if matriz_aumentada[j][i] != 0:
                    matriz_aumentada[i], matriz_aumentada[j] = matriz_aumentada[j], matriz_aumentada[i]
                    break
            else:
                return None  # Matriz não invertível (linha de zeros encontrada)

        # Torna o elemento pivô igual a 1
        pivo = matriz_aumentada[i][i]
        matriz_aumentada[i] = [Fraction(x, pivo) for x in matriz_aumentada[i]]

        # Zera os elementos abaixo e acima do pivô
        for j in range(n):
            if j != i:
                fator = matriz_aumentada[j][i]
                matriz_aumentada[j] = [x - fator * y for x, y in zip(matriz_aumentada[j], matriz_aumentada[i])]

    # Extrai a inversa (metade direita da matriz aumentada)
    inversa = [linha[n:] for linha in matriz_aumentada]
    return inversa

# Exemplo de uso (você pode substituir por sua própria matriz)
matriz = [[2, 1, 3], [5, 3, 4], [4, 8, 7]]
matriz_inversa = inversa_gauss_jordan(matriz)

if matriz_inversa is not None:
    print("Matriz inversa:")
    for linha in matriz_inversa:
        print([str(fracao) for fracao in linha])  # Imprime frações como strings
else:
    print("A matriz não é invertível.")