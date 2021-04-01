def merge_sort(lista,n=None):
    if n == None:
        fim = len(lista)
        inv1, inv2, inv = 0, 0, 0
        if n == 1:
            return 0
        inicio = 0
        meio = (fim + inicio)//2
        left = lista[inicio:meio]
        right = lista[meio:fim]
        inv1 += merge_sort(left)
        inv2 += merge_sort(right)
        topo_left, topo_right = 0, 0
        for k in range(inicio, fim):
            if topo_left >= len(left):
                lista[k] = right[topo_right]
                topo_right += 1
                inv += (len(left) - topo_left)

            elif topo_right >= len(right):
                lista[k] = left[topo_left]
                topo_left += 1

            elif left[topo_left] <= right[topo_right]:
                lista[k] = left[topo_left]
                topo_left += 1
            else:
                lista[k] = right[topo_right]
                topo_right += 1
                inv += (len(left)-topo_left)
        return inv+inv2+inv1

N = int(input())
A = [int(e) for e in input().split()]
print(merge_sort(A))

