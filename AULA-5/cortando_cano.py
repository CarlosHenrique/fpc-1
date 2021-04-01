def maior(a, b):
    maior = a
    if b > a:
        maior = b
    return maior

def mochila(T, tam_cano, valores, n):
    if n == 0 or T == 0:
        return 0

    if (tam_cano[n - 1] > T):
        return mochila(T, tam_cano, valores, n - 1)
    
    else:
        return maior(valores[n - 1] + mochila(T - tam_cano[n - 1], tam_cano, valores, n - 1),mochila(T, tam_cano, valores, n - 1))


N, T = [int(e) for e in input().split()]
valores, tam_cano = [], []
for i in range(N):
    cano, valor = [int(e) for e in input().split()]
    tam_cano.append(cano)
    valores.append(valor)
print(mochila(T, tam_cano, valores, N))


