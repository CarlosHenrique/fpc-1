
class No(): #no de listas duplamente encadedadas
    def __init__(self, dado=None):
        self._dado = dado
        self._prox = None
        self._ant = None

    def __str__(self):
        return '{}'.format(self._dado)

class Lista(): #lista duplamente encadeada
    def __init__(self):
        self._inicio = None
        self._fim = None

    def isVazia(self):
        if self._inicio == None:
            return True

        return False

    def inserirNoFim(self, dado=None):
        novono = No(dado)
        if self.isVazia():
            self._inicio = self._fim = novono
        else:
            novono._ant = self._fim
            self._fim._prox = novono
            self._fim = novono

    def buscar(self,x):
        i = self._inicio
        while i != None:
            if x == i._dado:
                break
            else:
                i = i._prox
        return i

    def __iter__(self):
        i = self._inicio
        while i != None:
            yield i._dado
            i = i._prox

    def remover(self, x):
        no_encontrado = self.buscar(x)
        if no_encontrado != None:
            if no_encontrado._ant != None:
                no_encontrado._ant._prox = no_encontrado._prox
            else:
                self._inicio = no_encontrado._prox
            if no_encontrado._prox != None:
                no_encontrado._prox._ant = no_encontrado._ant
            else:
                self._fim = no_encontrado._ant
        return no_encontrado

    def __str__(self):
        s = ""
        i = self._inicio
        while i != None:
            if i._prox == None:
                s += "{}".format(str(i))

            else:
                s += "{} ".format(str(i))
            i = i._prox
        return s

if __name__ == "__main__":
    lista_D = Lista()
    lista_E = Lista()
    pares = 0
    N = int(input())
    for x in range(N):
        M, L = input().split()
        if L == "D":
            lista_D.inserirNoFim(M)
        if L == "E":
            lista_E.inserirNoFim(M)
    for x in lista_D:
        if x in lista_E:
            lista_E.remover(x)
            pares += 1
    print(pares)
