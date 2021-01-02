def Permuta(num):
    if num != 0:
        soma = num
        for i in range(1, num):
            soma = soma*i
    else:
        soma = 1 
    
    return soma


def Arranjo(n, r):
    div = n-r
    resposta = Permuta(n)/ Permuta(div)

    return resposta


def CombinatoriaSimples(n, r):
    dividendo = Permuta(n)/Permuta(r)
    divisor = n-r

    resposta = dividendo / Permuta(divisor)

    return resposta


def Comb_Complementar(n, p):
    r = n - p

    return CombinatoriaSimples(n, r)


def Kaplansky(n, p):
    num = n-p+1

    return CombinatoriaSimples(num, p)


def InteirosPositivos(m, n):
    m = m-1
    n = n-1

    return CombinatoriaSimples(m, n)


def Nao_Negativos(m, n):
    m = m+n-1
    n = n-1

    return CombinatoriaSimples(m, n)


def Comb_Repeticao(n, p):
    r = n-1
    n = n+p-1

    return CombinatoriaSimples(n, r)


def Permuta_Repeticao(n, lista):
    soma = 1
    for i in range(0, len(lista)):
        r = lista[i]
        lista[i] = CombinatoriaSimples(n, r)
        n -= r
        soma *= lista[i]
    
    return soma


def Arranjo_Repeticao(m, p):

    return m**p


def Permuta_Circular(n):
    n = n-1

    return Permuta(n)


def Permuta_Caotica(n):

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
        
