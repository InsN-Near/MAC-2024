import sympy

def simplificar_fracao_avancado(expressao):
    """Tenta simplificar uma fração algébrica de forma mais avançada usando o sympy."""
    # Extrai as variáveis da expressão
    variaveis = expressao.free_symbols
    
    numerador, denominador = expressao.as_numer_denom()  # Separa numerador e denominador

    # Aplica simplificação no numerador e denominador separadamente
    numerador_simplificado = sympy.simplify(numerador)
    denominador_simplificado = sympy.simplify(denominador)

    # Tenta simplificar a fração como um todo
    fracao_simplificada = sympy.simplify(numerador_simplificado / denominador_simplificado)
    
    return fracao_simplificada

# Obtém a entrada do usuário
expressao_entrada = input("Digite a expressão algébrica para simplificar: ")

# Tenta simplificar a expressão
try:
    expressao_sympy = sympy.sympify(expressao_entrada)
    resultado = simplificar_fracao_avancado(expressao_sympy)
    print("Expressão simplificada:", resultado)
except sympy.SympifyError:
    print("Expressão inválida. Verifique a sintaxe.")