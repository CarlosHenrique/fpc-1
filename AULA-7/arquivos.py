def mergesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if (fim - inicio) > 1:
        meio = (fim + inicio) // 2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

    return lista

def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left = top_left + 1
        else:
            lista[k] = right[top_right]
            top_right = top_right + 1

def max_arq(lista, N, B):
    total = 0
    inicio, fim = 0, N-1
    while lista[inicio] + lista[fim] > B:
        total += 1
        fim -= 1

    while inicio <= fim and fim > 0 and inicio < (len(lista)-1):
        if lista[inicio] + lista[fim] <= B:
            fim -= 1
            inicio += 1
        elif lista[inicio] + lista[fim] > B:
            fim -= 1
        total += 1


    return total

N, B = [int(e) for e in input().split()]
print(max_arq(mergesort([int(e) for e in input().split()]), N, B))



