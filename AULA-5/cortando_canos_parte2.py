def mochila(T, valores, canos):
    matriz = [0 for i in range(T + 1)]

    start = min(canos)
    for i in range(start, T + 1):
        matriz[i] = matriz[i - 1]
        index = 0
        for valor in valores:
            if canos[index] <= i and matriz[i] < matriz[i - canos[index]] + valor:
                matriz[i] = matriz[i - canos[index]] + valor
                index += 1
            else:
                index += 1

    return matriz[T]

N, T = [int(e) for e in input().split()]
valores, canos = [], []
for i in range(N):
    cano, valor = [int(e) for e in input().split()]
    canos.append(cano)
    valores.append(valor)
print(mochila(T, valores, canos))