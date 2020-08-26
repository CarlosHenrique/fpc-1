def sucessor(a):
    return a+1

def soma(a,b):
    
    for i in range(b):
        a = sucessor(a)
    return a

def multiplicacao(a,b):
    c=0
    for i in range(b):
        c = soma(c,a)
    return c

def exponenciacao(a,b):
    c= 1
    for i in range(b):
        c = multiplicacao(c,a)
    return c       


while True:
    cmd = input()
    if cmd:
        cmd = cmd.split()
        if cmd[0] =="Suc":
            print(sucessor(int(cmd[1])))
        elif cmd[0] == 'Soma':
            print(soma(int(cmd[1]),int(cmd[2])))
        elif cmd[0] == 'Mult':
            print(multiplicacao(int(cmd[1]),int(cmd[2])))
        elif cmd[0] == "Exp":
            print(exponenciacao(int(cmd[1]),int(cmd[2])))
    else:
        break