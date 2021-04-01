class HashTable:
    def __init__(self):
        self.MAX = 20005
        self.arr = [None for i in range(self.MAX)]

    def hash(self, key):
        hash= int(key, 2)
        return hash % self.MAX

    def getitem(self, index):
        h = self.hash(index)
        if self.arr[h] is None:
            return False
        else:
            return self.arr[h]

    def setitem(self, key, val):
        h = self.hash(key)
        self.arr[h] = val

def maior(a, b):
    maior = a
    if b > a:
        maior = b
    return maior


M, N = [int(e) for e in input().split()]
planos = [[0 for i in range(4)] for _ in range(M)]
for i in range(M):
    planos[i][0], planos[i][1], planos[i][2], planos[i][3] = [int(e) for e in input().split()]
regioes = HashTable()
max = 0
for i in range(N):
    chave = ""
    x, y, z = [int(e) for e in input().split()]
    for i in range(M):
        if planos[i][0]*x+planos[i][1]*y+planos[i][2]*z > planos[i][3]:
            chave += "1"
        else:
            chave += "0"

    if regioes.getitem(chave) != False:
        regioes.setitem(chave, regioes.getitem(chave)+1)
    else:
        regioes.setitem(chave, 1)
    x = regioes.getitem(chave)
    max = maior(max, regioes.getitem(chave))

print(max)
