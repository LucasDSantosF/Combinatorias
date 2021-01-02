def Permuta(num):
    soma = num
    for i in range(1, num):
        soma = soma*i
    
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