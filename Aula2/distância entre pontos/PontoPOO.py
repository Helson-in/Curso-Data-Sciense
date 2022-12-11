class Ponto():
    def __init__(self):
        self.x = int(input("Digite valor de x: "))
        self.y = int(input("Digite valor de y: "))
            
    def distancia(self, x, x_outro, y, y_outro):
        distancia_ab = (((x_outro-x)**2)+((y_outro-y)**2))**1/2
        return distancia_ab
    
p = Ponto()
