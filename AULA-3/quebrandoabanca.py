def maior_numero(inicio, fim, lista):
    maior = 0
    for i in range(B+1):
        if len(lista[inicio:fim]) >= 1 and int(lista[inicio:fim]) > maior:
            maior = int(lista[inicio:fim])
            indice = int(inicio)
        inicio += 1
        fim += 1
    return(indice)


saldo_final = []

while True:
    try:
        A, B = tuple(map(int, input().split(' ')))
        saldo = input()
        si = 0
        sf = A - B
        final = ''
        for i in range(A - B):
            final += (saldo[maior_numero(si, sf, saldo)])
            si = maior_numero(si, sf, saldo) + 1
            sf = sf + 1
        saldo_final.append(final)

    except: break

for r in saldo_final:
  print(r)