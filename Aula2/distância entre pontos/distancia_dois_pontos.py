def dois_pontos():
    x1 = float(input("Digite a coordenada X1: "))
    x2 = float(input("Digite a coordenada X2: "))
    y1 = float(input("Digite a coordenada Y1: "))
    y2 = float(input("Digite a coordenada Y2: "))
    
    distancia_ab = (((x2-x1)**2)+((y2-y1)**2))**1/2
    
    return distancia_ab

def cinco_pontos():
    x1 = float(input("Digite a coordenada X1: "))
    y1 = float(input("Digite a coordenada Y1: "))
    
    for i in range(5):
        x2 = float(input("Digite a coordenada X{}: ".format(i+2)))
        y2 = float(input("Digite a coordenada Y{}: ".format(i+2)))
        distancia_ab = (((x2-x1)**2)+((y2-y1)**2))**1/2
        print(distancia_ab)

#dois_pontos()
#cinco_pontos()


# Poo chamando o método

x2 = float(input("Digite a coordenada X2: "))
y2 = float(input("Digite a coordenada Y2: "))

distania_ab = p.distancia(x1,x2,y1,y2)