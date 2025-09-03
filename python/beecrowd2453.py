frase = input()
saida = ""
i = 0

while i < len(frase):
    if frase[i] == "p":  # achou um 'p'
        if i + 1 < len(frase):   # garante que tem letra depois
            saida += frase[i+1]  # pega a letra depois do 'p'
            i += 2               # pula o 'p' e a letra
        else:
            i += 1               # só avança (caso raro no fim)
    else:
        saida += frase[i]        # copia normalmente
        i += 1

print(saida)