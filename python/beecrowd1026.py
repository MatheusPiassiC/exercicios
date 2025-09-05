def verifica_vagoes(ordem_saida):
    ordem_chegada = list()
    for i in range(len(ordem_saida)):
        ordem_chegada.append(i + 1)
    aux = list()
    while True:
        if(ordem_chegada.index[0] == ordem_saida[0]): #chega um vagao na ordem em que devia sair
            ordem_chegada.pop(0)
            ordem_saida.pop(0)
        elif(len(aux) > 0 and aux[len(aux) - 1] == ordem_saida[0]): #o trem que está na estação é o que deveria sair
            ordem_saida.pop(0)
            aux.pop(len(aux) - 1)
        elif(ordem_chegada.index[0] != ordem_saida[0]): #chega um vagao diferente do que devia sair
            aux.append(ordem_chegada.pop(0))

    

loop1 = True
while loop1:
    n = int(input())
    if(n != 0):
        vagoes = list()
        while vagoes != [0]:
            vagoes = list(map(int,input().split()))
            print(vagoes)
    else: 
        loop1 = False

