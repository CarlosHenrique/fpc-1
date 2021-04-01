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

N = int(input())
ident_n = input().split()
lista_p = Lista()
for e in ident_n:
    lista_p.inserirNoFim(e)
M = int(input())
ident_m = input().split()
lista_saida = Lista()
for e in ident_m:
    lista_p.remover(e)
print(lista_p)


