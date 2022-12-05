valores_pares = []

def pares(valores):
    for i in valores:
        if i % 2 == 0:
            valores_pares.append(i)
            print("{} é par".format(i))
        else:
            print("{} é impar".format(i))
pares([1,3,4,6,7,8,9,10])

        
print("foram digitados {} números pares.".format(len(valores_pares)))

