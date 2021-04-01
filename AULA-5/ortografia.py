def menor_custo(a,b,c):
    menor = a
    if b < a and b < c:
        menor = b
    if c < a and c < b:
        menor = c
    return menor

def distancia_edicao(p1, p2):
    tamanho1 = len(p1)
    tamanho2 = len(p2)
    if tamanho1 > tamanho2:
        p1, p2 = p2, p1
    distancia = range(tamanho1 + 1)
    index1, index2 = 0,0
    for S in p2:
        distancia2 = [index2+1]
        for T in p1:
            if T == S:
                distancia2 += [distancia[index1]]
            else:
                distancia2 += [1 + menor_custo((distancia[index1]), (distancia[index1 + 1]), (distancia2[-1]))]
            index1 += 1
        index1 = 0
        index2 += 1
        distancia = distancia2
    return distancia[-1]



n, m = [int(c) for c in input().split()]
dicionario = [input() for x in range(n)]
p_erradas = [input() for x in range(m)]

n_palavras = len(p_erradas)
cont = 0
while cont < n_palavras:
    lista = []
    for n in dicionario:
        if len(n) <= len(p_erradas[cont]) + 2 or len(n) < len(p_erradas[cont]) + 2:
            if distancia_edicao(p_erradas[cont], n) <= 2:
                lista += [n]
        else:
            pass
    p_erradas[cont] = lista
    print(' '.join(p_erradas[cont]), end="")
    if p_erradas[cont] != p_erradas[-1]:
        print("", end='')
    print('')
    cont+=1

