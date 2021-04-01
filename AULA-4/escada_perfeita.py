n = int(input())
x = input().split()
pilha = []
total_blocos = 0
for i in x:
    pilha.append(int(i))
    total_blocos += int(i)
b = ((2 * (total_blocos) // n)+n-1)//2  # termo geral da pa  = ultimo bloco
a = 1+b-n  # a1 da pa = primeiro bloco

sub_moves, all_moves = 0, 0
index = 0
if a <= 0: # se meu primeiro bloco for negativo ou igual a 0, não da p fazer a escada
    print(-1)
else:
    for i in range(n):
        if pilha[index] > a: # aqui eu subtraio e adiciono o n de movimentos de retirada
            aux = pilha[index]
            pilha[index] = a
            sub_moves += aux - a
            all_moves += aux - a #aqui eu adiciono os blocos q retirei
        else:
            aux = pilha[index]
            pilha[index] = a
            all_moves += aux-a #aqui eu subtraio os blocos q coloquei dos q retirei
        a += 1
        index += 1

    if all_moves != 0: # se essa variavel for igual a zero, eu printo a quantidade de movimentos necessarias
        # se n for eu print -1 , pois faltaram/sobraram pedras
        print(-1)
    else:
        print(sub_moves)
