class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None

def build_tree(pre_order: list, in_order: list):
    if not pre_order or not in_order:
        return None

    raiz_val = pre_order[0]
    raiz = Node(raiz_val)

    index = in_order.index(raiz_val)
    
    in_esq = in_order[:index]
    in_dir = in_order[index+1:]

    tam_esq = len(in_esq)

    pre_esq = pre_order[1:1+tam_esq]
    pre_dir = pre_order[1+tam_esq:]

    raiz.esq = build_tree(pre_esq, in_esq)
    raiz.dir = build_tree(pre_dir, in_dir)

    return raiz

def pos_ordem(no):
    if no is None:
        return ""
    return pos_ordem(no.esq) + pos_ordem(no.dir) + no.valor

n_entradas = int(input())
saidas = list()
for i in range(n_entradas):
    entrada = input().split()
    entrada_pre_order = entrada[1]
    entrada_in_order = entrada[2]
    no = build_tree(entrada_pre_order,entrada_in_order)
    saidas.append(pos_ordem(no))

for i in range(n_entradas):
    print(saidas[i])




    


# na ordenação pré-ordem (raiz, esquerda, direita), a raiz sempre é o primeiro item
# na ordenação em ordem (esquerda, raiz, direita), a raiz divide a arvore esquerda e direita
# a partir disso, podemos fazer a ordenação pós-ordem (direita, raiz, esquerda)