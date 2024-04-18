def binomial(n, k):
    """Calcula o coeficiente binomial usando a fórmula de combinação."""
    if k < 0 or k > n:
        return 0
    result = 1
    for i in range(1, min(k, n - k) + 1):
        result *= (n - i + 1)
        result //= i
    return result

def expandir_binomio(expressao):
    """Expande um binômio usando o teorema binomial."""
    termos = expressao.split('^')
    if len(termos) != 2:
        raise ValueError("Expressão inválida. O formato deve ser '(a + b)^n'")
    base, expoente = termos[0].strip(), int(termos[1])
    a, b = base[1:-1].split('+')  # Extrai 'a' e 'b' da base (a + b)

    resultado = []
    for k in range(expoente + 1):
        coeficiente = binomial(expoente, k)
        termo = f"{coeficiente} * {a}^{expoente - k} * {b}^{k}"
        resultado.append(termo)

    return ' + '.join(resultado)

# Exemplo de uso:
expressao = "(x + y)^4"
resultado = expandir_binomio(expressao)
print(f"Expansão de {expressao}: {resultado}")