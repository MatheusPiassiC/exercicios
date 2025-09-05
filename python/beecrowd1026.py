def verifica_vagoes(ordem_saida):
    n = len(ordem_saida)
    ordem_chegada = list(range(1, n + 1))  #trem vindo de A
    pilha = []                             #estação (stack)
    ordem_saida = ordem_saida.copy()       #para não destruir a lista original
    
    while ordem_chegada or pilha:
        
        if pilha and pilha[-1] == ordem_saida[0]: #se o topo da pilha é o próximo da saída, manda embora
            pilha.pop()
            ordem_saida.pop(0)
        elif ordem_chegada:                       #se ainda tenho vagões chegando, empurra pra pilha
            pilha.append(ordem_chegada.pop(0))
        else:
            break
    
    return len(ordem_saida) == 0


    

loop1 = True
while loop1:
    n = int(input())
    if n == 0:  
        loop1 = False
        break

    while True:
        vagoes = list(map(int, input().split()))
        if vagoes == [0]:  
            print()
            break

        if verifica_vagoes(vagoes):
            print("Yes")
        else:
            print("No")

