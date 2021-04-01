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

    def removerElemento(self, x):
        no_encontrado = self.buscar(x)
        if no_encontrado != None:
            if no_encontrado._ant != None:
                no_encontrado._ant._prox = no_encontrado._prox
            if no_encontrado._prox != None:
                no_encontrado._prox._ant = no_encontrado._ant
        return no_encontrado

    def removerDoInicio(self):
        no = self._inicio
        if not self.isVazia():
            if no._prox == None:
                self._fim = None
            else:
                no._prox._ant = None
            self._inicio = no._prox
        return no._dado

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

class Fila(Lista):
    def inserir(self,dado):
        self.inserirNoFim(dado)
    def remover(self):
        return self.removerDoInicio()

class Pilha(Lista):
    def push(self, dado=None):
        novono = No(dado)
        if self.isVazia():
            self._fim = novono
        else:
            novono._prox = self._inicio
            self._inicio._ant = novono
        self._inicio = novono

    def pop(self):
        return self.removerDoInicio()

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        pilha = Pilha()
        n = input()
        for e in n:
            if e == '{' or e == '[' or e == '(':
                pilha.push(e)
            else:
                if e == '}' and (pilha.isVazia() == False) and str(pilha._inicio) == '{':

                    pilha.pop()
                elif e == ']' and (pilha.isVazia() == False) and str(pilha._inicio) == '[':

                    pilha.pop()
                elif e == ')' and (pilha.isVazia() == False) and str(pilha._inicio) == '(':

                    pilha.pop()
                elif e == '}' or e == ']' or e == ')':
                    pilha.push(e)
                    break
        if pilha.isVazia():
            print('S')
        else:
            print('N')