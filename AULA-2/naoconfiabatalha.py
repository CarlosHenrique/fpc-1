
def ler_barco(L,C):
    # barco a baixo
    global tabuleiro,tam_barco

    if (L+1 <= len(tabuleiro)-1):
        if tabuleiro[L+1][C] == "#":
            tabuleiro[L+1][C] = barco
            ler_barco(L+1,C)
            tam_barco += 1
    # barco a cima
    if L-1 >= 0:
        if tabuleiro[L-1][C] == "#":
            tabuleiro[L-1][C] = barco
            ler_barco( L-1,C)
            tam_barco += 1
    # barco a direita
    if C+1 <= len(tabuleiro[L])-1:
        if tabuleiro[L][C+1] == "#":
            tabuleiro[L][C+1] = barco
            ler_barco(L, C+1)
            tam_barco += 1
    # barco a esquerda
    if C-1 >= 0:
        if tabuleiro[L][C-1] == "#":
            tabuleiro[L][C-1] = barco
            ler_barco(L, C - 1)
            tam_barco += 1


def checa_tiros(L,C):
    index_tiro = tabuleiro[L][C]
    lista_barcos[index_tiro-1] -= 1




L,C = [int(x) for x in input().split()]
tabuleiro = []
for x in range(L):
    linha = []
    coluna = input()
    for j in coluna:
        linha.append(j)
    tabuleiro.append(linha)

barco = 1
tam_barco = 1
lista_barcos = []
barco_destruido = 0

Qnt = int(input()) # quant de tiros
tiros = []
for i in range(Qnt):
    L,C=input().split()
    L = int(L)-1
    C = int(C)-1
    if tabuleiro[L][C] == ".":
        pass
    elif tabuleiro[L][C] == "#":
        tabuleiro[L][C] = barco
        ler_barco(L,C)
        lista_barcos.append(tam_barco)
        tam_barco = 1
        barco+=1
        checa_tiros(L, C)
    else:
        checa_tiros(L, C)



for i in lista_barcos:
    if i == 0:
        barco_destruido += 1

print(barco_destruido)