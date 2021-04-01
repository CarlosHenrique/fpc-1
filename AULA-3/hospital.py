def orderna_os_planos(pacientes):
    premium, diamante, ouro, prata, bronze, resto = [], [], [], [], [], []
    for paciente in pacientes:
        if paciente[1] == "premium":
            premium.append(paciente)
        elif paciente[1] == 'diamante':
            diamante.append(paciente)
        elif paciente[1] == 'ouro':
            ouro.append(paciente)
        elif paciente[1] == 'prata':
            prata.append(paciente)
        elif paciente[1] == 'bronze':
            bronze.append(paciente)
        elif paciente[1] == 'resto':
            resto.append(paciente)

    return list(filter(lambda i: len(i) > 0, [premium, diamante, ouro, prata, bronze, resto]))
    #se a lista do plano tiver vazia não retorna
    #retorna a lista de pacientes em ordem por plano

def ordena_a_gravidade(lista_paciente):
    for plano in range(len(lista_paciente)):
        for posi_paciente in range(1, len(lista_paciente[plano])):
            paciente_atual = lista_paciente[plano][posi_paciente]
            paciente = posi_paciente - 1
            while paciente >= 0 and int(lista_paciente[plano][paciente][2]) < int(paciente_atual[2]):
                lista_paciente[plano][paciente + 1] = lista_paciente[plano][paciente]
                paciente -= 1
                lista_paciente[plano][paciente + 1] = paciente_atual
    return lista_paciente

def ordem_alfabetica(lista_paciente):
    for plano in range(len(lista_paciente)):
        for posi_paciente in range(1, len(lista_paciente[plano])):
            paciente_atual = lista_paciente[plano][posi_paciente]
            paciente = posi_paciente - 1
            try:
                if int(lista_paciente[plano][paciente][2]) == int(paciente_atual[2]):
                    while paciente >= 0 and lista_paciente[plano][paciente][0] > paciente_atual[0]:
                        lista_paciente[plano][paciente + 1] = lista_paciente[plano][paciente]
                        paciente -= 1
                        lista_paciente[plano][paciente + 1] = paciente_atual
            except IndexError:
                pass
    return lista_pacientes


pacientes = []
n_pacientes = int(input())
for i in range(n_pacientes):
    dados = input().split()
    pacientes.append((dados))
lista_pacientes = orderna_os_planos(pacientes)
print(lista_pacientes)
ordena_a_gravidade(lista_pacientes)
print(lista_pacientes)
ordem_alfabetica(lista_pacientes)
print(lista_pacientes)

for lista_planos in lista_pacientes:
    for paciente in lista_planos:
        print(paciente[0])


