import itertools

def negacao(p):
    return not p

def conjuncao(*args):
    return all(args)

def disjuncao(*args):
    return any(args)

def condicional(p, q, *args):
    # Para mais de duas proposições, a condicional é aplicada sequencialmente
    # Exemplo: P → Q → R é interpretado como (P → Q) ∧ (Q → R)
    if not args:
        return not p or q
    return condicional(p, q) and condicional(q, args[0], *args[1:])

def bicondicional(p, q, *args):
    # Para mais de duas proposições, a bicondicional é aplicada sequencialmente
    # Exemplo: P ↔ Q ↔ R é interpretado como (P ↔ Q) ∧ (Q ↔ R)
    if not args:
        return p == q
    return bicondicional(p, q) and bicondicional(q, args[0], *args[1:])

def gerar_tabela_verdade(n):
    if n < 1 or n > 9:
        print("Número de proposições deve ser entre 1 e 9.")
        return
    
    # Gera todas as combinações possíveis de verdadeiro e falso para n proposições
    combinacoes = list(itertools.product([True, False], repeat=n))
    
    # Cabeçalho da tabela
    letras_proposicoes = ['P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X']
    proposicoes = letras_proposicoes[:n]
    operacoes = ['~P', 'P ∧ ...', 'P ∨ ...', 'P → ...', 'P ↔ ...']
    print(' | '.join(proposicoes + operacoes))
    print('-' * (9 * (len(proposicoes) + len(operacoes)) - 1))
    
    # Corpo da tabela
    for combinacao in combinacoes:
        resultados = [
            negacao(combinacao[0]),
            conjuncao(*combinacao),
            disjuncao(*combinacao),
            condicional(*combinacao),
            bicondicional(*combinacao)
        ]
        linha = combinacao + tuple(resultados)
        print(' | '.join(['V' if val else 'F' for val in linha]))

# Exemplo de uso
gerar_tabela_verdade(2)  # Altere o número para gerar tabelas para diferentes quantidades de proposições