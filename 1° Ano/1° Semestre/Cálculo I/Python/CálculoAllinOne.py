import sympy as sp


def calcular_limite():
    expr = input("Digite a expressão para o limite (ex: sin(x)/x): ")
    ponto_str = input("Digite o ponto que x tende a (use 'inf' para infinito): ")
    x = sp.symbols('x')
    f = sp.sympify(expr)
    ponto = sp.oo if ponto_str == 'inf' else float(ponto_str) 
    limite = sp.limit(f, x, ponto)
    print(f"O limite de {expr} quando x tende a {ponto_str} é: {limite}")

def calcular_derivada():
    expr = input("Digite a expressão para derivar (ex: x**2 + 3*x + 2): ")
    x = sp.symbols('x')
    f = sp.sympify(expr)
    derivada = sp.diff(f, x)
    print(f"A derivada de {expr} é: {derivada}")

def calcular_integral():
    expr = input("Digite a expressão para integrar (ex: x**2): ")
    x = sp.symbols('x')
    f = sp.sympify(expr)
    integral = sp.integrate(f, x)
    print(f"A integral de {expr} é: {integral}")

def aproximar_taylor():
    expr = input("Digite a expressão para aproximar (ex: exp(x)): ")
    ordem = int(input("Digite a ordem da série de Taylor: "))
    x = sp.symbols('x')
    f = sp.sympify(expr)
    taylor = sp.series(f, x, 0, ordem+1).removeO()
    print(f"A aproximação de Taylor de {expr} até a ordem {ordem} é: {taylor}")

def metodo_newton_raphson():
    expr = input("Digite a expressão da função (ex: x**2 - 2): ")
    x0 = float(input("Digite o valor inicial para x: "))
    x = sp.symbols('x')
    f_expr = sp.sympify(expr)
    df_expr = sp.diff(f_expr, x)  
    f = sp.lambdify(x, f_expr)
    df = sp.lambdify(x, df_expr)
    raiz = newton_raphson(f, df, x0)
    print(f"A raiz encontrada pelo método de Newton-Raphson é: {raiz}, usando a derivada {df_expr}")

def newton_raphson(f, df, x0, tol=1e-5, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

if __name__ == "__main__":
    print("Escolha uma opção: ")
    print("1. Limites")
    print("2. Derivadas")
    print("3. Integração")
    print("4. Aproximação de Séries de Taylor")
    print("5. Método de Newton-Raphson")
    escolha = input("Digite o número da opção desejada: ")

    if escolha == '1':
        calcular_limite()
    elif escolha == '2':
        calcular_derivada()
    elif escolha == '3':
        calcular_integral()
    elif escolha == '4':
        aproximar_taylor()
    elif escolha == '5':
        metodo_newton_raphson()
    else:
        print("Opção inválida.")


