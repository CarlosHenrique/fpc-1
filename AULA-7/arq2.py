def mergesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if(fim - inicio > 1):
        meio = (fim + inicio)//2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

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
    arquivos = 0
    inicio, fim = 0, N-1
    while fim > 0 and inicio < N - 1:
        if lista[inicio] == 0:
            inicio += 1
        if lista[inicio] + lista[fim] > B:
            lista[fim] = 0
            fim -= 1
        else:
            if fim > inicio:
                lista[inicio],lista[fim] = 0,0
                arquivos += 1
                fim -= 1
    return arquivos

N, B = [int(e) for e in input().split()]
lista = [int(e) for e in input().split()]
mergesort(lista)
print(max_arq(lista, N, B))