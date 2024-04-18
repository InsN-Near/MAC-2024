def convert_from_decimal(number, base):
    """
    Converte um número decimal para uma base específica.
    """
    if base == 10:
        return str(number)
    elif base == 2:
        return bin(number)[2:]
    elif base == 16:
        return hex(number)[2:]
    elif base == 60:
        # Conversão para base sexagesimal (base 60)
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        if number < 0:
            return '-' + convert_from_decimal(-number, base)
        result = ''
        while number > 0:
            number, remainder = divmod(number, base)
            result = digits[remainder] + result
        return result or '0'
    else:
        raise ValueError("Base não suportada.")

def convert_to_decimal(number, base):
    """
    Converte um número de uma base específica para decimal.
    """
    if base == 10:
        return int(number)
    elif base == 2:
        return int(number, 2)
    elif base == 16:
        return int(number, 16)
    elif base == 60:
        # Conversão de base sexagesimal (base 60) para decimal
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        decimal = 0
        for digit in number:
            decimal = decimal * base + digits.index(digit)
        return decimal
    else:
        raise ValueError("Base não suportada.")

def main():
    number = input("Digite o número para conversão: ")
    base_origem = int(input("Digite a base de origem (2, 10, 16, 60): "))
    base_destino = int(input("Digite a base de destino (2, 10, 16, 60): "))

    if base_origem != 10:
        # Primeiro converte para decimal
        number_in_decimal = convert_to_decimal(number, base_origem)
    else:
        number_in_decimal = int(number)

    # Depois converte do decimal para a base de destino
    result = convert_from_decimal(number_in_decimal, base_destino)

    print(f"Resultado da conversão: {result}")

if __name__ == "__main__":
    main()