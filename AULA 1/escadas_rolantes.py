pessoas = int(input())

lista = []
for i in range(pessoas):
    enter_time = int(input())
    lista.append(enter_time)

inicio = lista[0]
indice = len(lista) - 1
final = lista[indice]
resultado = int(final - inicio + 10)
print(resultado)
