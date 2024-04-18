import sympy

def fatorar_expressao(expressao):
    """Fatora uma expressão algébrica usando o sympy."""
    # Identifica os símbolos (variáveis) na expressão
    simbolos = sorted(list(set(filter(str.isalpha, expressao))))
    # Cria os símbolos dinamicamente
    variaveis = sympy.symbols(simbolos)
    # Cria um dicionário para mapear string para símbolo
    variaveis_dict = dict(zip(simbolos, variaveis))
    
    # Substitui as variáveis na expressão pelo símbolo correspondente
    expressao_com_simbolos = expressao
    for simbolo in simbolos:
        expressao_com_simbolos = expressao_com_simbolos.replace(simbolo, f"variaveis_dict['{simbolo}']")
    
    expressao_simplificada = sympy.simplify(eval(expressao_com_simbolos))
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
except Exception as e:
    print(f"Ocorreu um erro: {e}")