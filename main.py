pares = []

for i in range(5):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        pares.append(num)
        print("{} é par".format(num))
    else:
        print("{} é impar".format(num))
        
print("foram digitados {} números pares.".format(len(pares)))