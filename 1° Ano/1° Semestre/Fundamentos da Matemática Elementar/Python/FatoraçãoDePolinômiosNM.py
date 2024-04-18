import sympy

def fatorar_expressao(expressao):
    """Fatora uma expressão algébrica usando o sympy."""
    x = sympy.Symbol('x')  # Define 'x' como um símbolo para a expressão
    expressao_simplificada = sympy.simplify(expressao)
    expressao_fatorada = sympy.factor(expressao_simplificada)
    return expressao_fatorada

# Obtém a entrada do usuário
expressao_entrada = input("Digite a expressão algébrica para fatorar: ")

# Tenta fatorar a expressão
try:
    resultado = fatorar_expressao(expressao_entrada)
    print("Expressão fatorada:", resultado)
except sympy.SympifyError:
    print("Expressão inválida. Verifique a sintaxe.")