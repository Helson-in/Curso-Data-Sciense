class Circunferencia():
    def __init__(self, p, raio):
        self.centro = p
        self.r = raio
    
    def pertence(self, p):
        if self.centro.distancia(p) <= self.r:
            return True
        else:
            return False
        
    