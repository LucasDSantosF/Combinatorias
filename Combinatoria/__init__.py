def Permuta(num):
    """
    param num: número de elementos distintos.
    """
    if num > 0:
        soma = num
        for i in range(1, num):
            soma = soma*i
    else:
        if num == 0:
            soma = 1
        else:
            return f"\033[;1m [Erro] \033[0;0m Só é possivel permutação de numeros positivos."

    
    return soma


def Arranjo(n, r):
    """
    param n : númetro de elementos distintos. \n
    param r : grupo de elementos do conjunto n.
    """
    div = n-r
    resposta = Permuta(n)/ Permuta(div)

    return resposta


def CombinacaoSimples(n, r):
    """
    param n : número de elemento distintos. \n
    param r : número de elemento tomados r a r do conjunto n.
    """
    dividendo = Permuta(n)/Permuta(r)
    divisor = n-r

    resposta = dividendo / Permuta(divisor)

    return resposta


def Comb_Complementar(n, p):
    """
    param n : número de elemento distintos. \n
    param p : número de elemento tomados n-p a n-p do conjunto n.
    """
    r = n - p

    return CombinatoriaSimples(n, r)


def Kaplansky(n, p):
    """
    param n : número de elemento distintos. \n
    param p : número de elemento tomados p a p do conjunto n.
    """
    num = n-p+1

    return CombinatoriaSimples(num, p)


def InteirosPositivos(m, n):
    """
    param m : valor da final da equação. \n
    param n : número de variáveis da equação.
    """
    m = m-1
    n = n-1

    return CombinatoriaSimples(m, n)


def Nao_Negativos(m, n):
    """
    param m : valor da final da equação. \n
    param n : número de variáveis da equação.
    """
    m = m+n-1
    n = n-1

    return CombinatoriaSimples(m, n)


def Comb_Repeticao(n, p):
    """
    param n : número de elemento distintos. \n
    param p : número de elemento tomados p a p do conjunto n.
    """
    r = n-1
    n = n+p-1

    return CombinatoriaSimples(n, r)


def Permuta_Repeticao(n, lista):
    """
    param n : número de elemento distintos. \n
    param lista : lista com o número de elementos de cada condição.
    """
    soma = 1
    for i in range(0, len(lista)):
        r = lista[i]
        lista[i] = CombinatoriaSimples(n, r)
        n -= r
        soma *= lista[i]
    
    return soma


def Arranjo_Repeticao(m, p):
    """
    param m : número de elemetos distintos. \n
    param p : número de vezes que m é repetido.
    """

    return m**p


def Permuta_Circular(n):
    """
    param n : número de elementos distintos.
    """
    n = n-1

    return Permuta(n)


def Permuta_Caotica(n):
    """
    param n : número de elementos distintos.
    """

    lista = []

    for i in range(0, n+1):
        lista.append(Permuta(i))
    
    aux = 1
    soma = 0
    num = Permuta(n)
    for i in range(0, len(lista)):
        if aux%2 == 1:
            soma += num/lista[i]
        else:
            soma -= num/lista[i]
        
        aux += 1
    
    return soma
        
