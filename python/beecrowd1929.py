def validateTriangle(a,b,c):
    a2 = (a < b + c)
    b2 = (b < a + c)
    c2 = (c < b + a) 
    if(a2 and b2 and c2): return True
    else: return False
        

def main():
    entrada = list(map(int,input().split()))
   

    for i in range(4):
        triangulo = entrada[:i] + entrada[i+1:]
        if(validateTriangle(triangulo[0],triangulo[1],triangulo[2])):
            print("S")
            break
    else: print("N")
    # i = 0  -> 1 2 3
    # i = 1  -> 0 2 3
    # i = 2  -> 0 1 3
    # i = 3  -> 1 2 3 
        

if __name__ == "__main__":
    main()





