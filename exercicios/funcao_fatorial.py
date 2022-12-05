def fatorial(num):
    fatorial = 1

    for i in range(num):
         fatorial = fatorial * (i+1)
    print("Resultado fatorial: {}".format(fatorial))
        
fatorial(4)