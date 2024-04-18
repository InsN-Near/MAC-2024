def sexagesimal_para_decimal(sexagesimal_str):
    """Converte uma string sexagesimal para um número decimal."""
    componentes = [int(x) for x in sexagesimal_str.split()]
    decimal = 0
    for i, componente in enumerate(reversed(componentes)):
        decimal += componente * 60**i
    return decimal

def decimal_para_sexagesimal(decimal_num):
    """Converte um número decimal para uma string sexagesimal."""
    componentes = []
    while decimal_num > 0:
        componente = decimal_num % 60
        componentes.append(componente)
        decimal_num //= 60
    sexagesimal_str = " ".join(str(x) for x in reversed(componentes))
    return sexagesimal_str

# Exemplos de uso
sexagesimal_num = "60 60 60 60"
decimal_num = sexagesimal_para_decimal(sexagesimal_num)
print(f"Sexagesimal: {sexagesimal_num}, Decimal: {decimal_num}")

decimal_num = 123456789
sexagesimal_num = decimal_para_sexagesimal(decimal_num)
print(f"Decimal: {decimal_num}, Sexagesimal: {sexagesimal_num}")
