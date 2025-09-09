
def tipo_triangulo(list):

    
    if list[2] >= (list[1] + list[0]):
        print("NAO FORMA TRIANGULO")
        return "erro"

    if list[2] == (list[1]**2 + list[0]**2)**0.5:
        print("TRIANGULO RETANGULO")
    elif list[2] > (list[1]**2 + list[0]**2)**0.5:
        print("TRIANGULO OBTUSANGULO")
    elif list[2] < (list[1]**2 + list[0]**2)**0.5:
        print("TRIANGULO ACUTANGULO")

    if list[2] == list[1] and list[1] == list[0]:
        print("TRIANGULO EQUILATERO")    
    elif list[2] == list[1] or list[1] == list[0] or list[0] == list[2]:
        print("TRIANGULO ISOSCELES")

    return "tudo certo!"



entrada = list(map(float, input().split()))
entrada.sort()
tipo_triangulo(entrada)