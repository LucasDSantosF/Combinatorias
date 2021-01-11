def Permutacao(num):
    """
    param num: número de elementos distintos. \n
    return : se for retornado o valor -1 quer dizer que ouve um erro.
    """
    if num > 0:
        soma = num
        for i in range(1, num):
            soma = soma*i
        
        return soma
    else:
        if num == 0:
            soma = 1
            return soma
        else:
            return -1


def Arranjo(n, r):
    """
    param n : númetro de elementos distintos. \n
    param r : grupo de elementos do conjunto n. \n
    return : se for retornado o valor -1 quer dizer que ouve um erro.
    """
    if n < 0 or r < 0:
        return -1
    else:
        div = n-r
        
        n = Permutacao(n)
        div = Permutacao(div)

        if n != -1 and div != -1:
            res = n / div
            return int(res)
        else:
            return -1


def CombinacaoSimples(n, r):
    """
    param n : número de elemento distintos. \n
    param r : número de elemento tomados r a r do conjunto n. \n
    return : se for retornado o valor -1 quer dizer que ouve um erro.
    """
    if n < 0 or r < 0:
        return -1
    else:
        dividendo = Permutacao(n)/Permutacao(r)
        divisor = n-r

        resposta = dividendo / Permutacao(divisor)

        return int(resposta)


def Comb_Complementar(n, p):
    """
    param n : número de elemento distintos. \n
    param p : número de elemento tomados n-p a n-p do conjunto n. \n
    return : se for retornado o valor -1 quer dizer que ouve um erro.
    """
    if n < 0 or p < 0:
        return -1
    else:
        r = n - p
        res = CombinacaoSimples(n, r)
        if res == -1:
            return -1
        else:
            return int(res)


def Kaplansky(n, p):
    """
    param n : número de elemento distintos. \n
    param p : número de elemento tomados p a p do conjunto n. \n
    return : se for retornado o valor -1 quer dizer que ouve um erro.
    """
    num = n-p+1

    res = CombinacaoSimples(num, p) 
    if res != -1:
        return int(res)
    else:
        return -1


def InteirosPositivos(m, n):
    """
    param m : valor da final da equação. \n
    param n : número de variáveis da equação. \n
    return : se for retornado o valor -1 quer dizer que ouve um erro.
    """
    m = m-1
    n = n-1

    res = CombinacaoSimples(m, n)
    if res != -1:
        return int(res)
    else:
        return -1


def Nao_Negativos(m, n):
    """
    param m : valor da final da equação. \n
    param n : número de variáveis da equação.
    """
    m = m+n-1
    n = n-1

    res = CombinacaoSimples(m, n)
    if res != -1:
        return int(res)
    else:
        return -1


def Comb_Repeticao(n, p):
    """
    param n : número de elemento distintos. \n
    param p : número de elemento tomados p a p do conjunto n. \n
    return : se for retornado o valor -1 quer dizer que ouve um erro.
    """
    r = n-1
    n = n+p-1

    res = CombinacaoSimples(n, r)
    if res != -1:
        return int(res)
    else:
        return -1


def Permutacao_Repeticao(n, lista):
    """
    param n : número de elemento distintos. \n
    param lista : lista com o número de elementos de cada condição. \n
    return : se for retornado o valor -1 quer dizer que ouve um erro.
    """
    soma = 1
    cont = 0
    for i in range(0, len(lista)):
        if lista[i] >= 0:
            r = lista[i]
            res = CombinacaoSimples(n, r)
            if res != -1:
                lista[i] = int(res)
                n -= r
                soma *= lista[i]
        else:
            cont += 1
    if soma == 1 and cont == len(lista):
        return -1
    else:
        return soma


def Arranjo_Repeticao(m, p):
    """
    param m : número de elemetos distintos. \n
    param p : número de vezes que m é repetido. \n
    return : se for retornado o valor -1 quer dizer que ouve um erro.
    """
    if p < 0 or m < 0:
       return -1
    else:
        return m**p


def Permutacao_Circular(n):
    """
    param n : número de elementos distintos. \n
    return : se for retornado o valor -1 quer dizer que ouve um erro.
    """
    n = n-1

    return Permutacao(n)


def Permutacao_Caotica(n):
    """
    param n : número de elementos distintos. \n
    return : se for retornado o valor -1 quer dizer que ouve um erro.
    """
    if n >= 0: 
        lista = []

        for i in range(0, n+1):
            lista.append(Permutacao(i))
    
        aux = 1
        soma = 0
        num = Permutacao(n)
        for i in range(0, len(lista)):
            if aux%2 == 1:
                soma += num/lista[i]
            else:
                soma -= num/lista[i]
        
            aux += 1
    
        return soma
    else:
        return -1
        
