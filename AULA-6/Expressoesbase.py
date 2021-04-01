class No():
    def __init__(self,dado=None):
        self.dado = dado
        self.prox = None
        self.ant = None

    def __str__(self):
        return f'{self.dado}'

class Lista():
    def __init__(self):
        self.inicio = None
        self.fim = None

    def isVazia(self):
        if self.inicio == None:
            return True
        return False

    def inserirNoFim(self,dado=None):
        novono = No(dado)
        if self.isVazia():
            self.inicio = self.fim = novono
        else:
            novono.ant = self.fim
            self.fim.prox = novono
            self.fim = novono

    def buscar(self,x):
        i = self.inicio
        while i != None:
            if x == i.dado:
                break
            else:
                i = i.prox
        return i

    def esvaziar(self):
        self.inicio = self.fim = None

    def removerElemento(self,x):
        no_encontrado = self.buscar(x)
        if no_encontrado != None:
            if no_encontrado.ant != None:
                no_encontrado.ant.prox= no_encontrado.prox
            else:
                self.inicio = no_encontrado.prox
            if no_encontrado.prox != None:
                no_encontrado.prox.ant = no_encontrado.ant
            else:
                self.fim = no_encontrado.ant
        return no_encontrado

    def removerDoInicio(self):
        no = self.inicio
        if not self.isVazia():
            if no.prox == None:
                self.fim = None
            else:
                no.prox.ant = None
            self.inicio = no.prox

        return no.dado

    def __str__(self):
        s = ''
        i = self.inicio
        while i != None:
            s += f'{str(i)}'
            i = i.prox
        return s

class Fila(Lista):
    def inserir(self,dado):
        self.inserirNoFim(dado)

    def remover(self):
        return self.removerDoInicio()
    def __str__(self):
        return '' + super().__str__()


class Pilha(Lista):
    def push(self, dado=None):
        novono = No(dado)
        if self.isVazia():
            self.fim = novono
        else:
            novono.prox = self.inicio
            self.inicio.ant = novono
        self.inicio = novono

    def pop(self):
        return self.removerDoInicio()

    def __str__(self):
        return '' + super().__str__()

if __name__ == '__main__':

    minhapilha_aberto = Pilha()
    minhapilha_fechado = Pilha()
    quant = int(input())
    cochete = ']'
    parentese = ')'
    chave = '}'

    i = 0
    for u in range(quant):
        entrada = str(input())
        for c in entrada:
            if c == '{':
                minhapilha_aberto.push('{')
            elif c == '[':
                minhapilha_aberto.push('[')
            elif c == '(':
                minhapilha_aberto.push('(')
            else:
                minhapilha_fechado.push(c)

                if str(minhapilha_aberto.inicio) == '{' and str(minhapilha_fechado.inicio) == '}':
                    minhapilha_aberto.pop()
                    minhapilha_fechado.pop()
                elif str(minhapilha_aberto.inicio) == '[' and str(minhapilha_fechado.inicio) == ']':
                    minhapilha_aberto.pop()
                    minhapilha_fechado.pop()
                elif str(minhapilha_aberto.inicio) == '(' and str(minhapilha_fechado.inicio) == ')':
                    minhapilha_aberto.pop()
                    minhapilha_fechado.pop()
                else:
                    break

        if minhapilha_aberto.isVazia() and minhapilha_fechado.isVazia():
            print('S')
            minhapilha_aberto.esvaziar()
            minhapilha_fechado.esvaziar()
        else:
            print('N')
            minhapilha_aberto.esvaziar()
            minhapilha_fechado.esvaziar()
