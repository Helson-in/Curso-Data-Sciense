palavra_invertida = []

def reverse(palavra):
    for i in range(len(palavra)):
        palavra_invertida.append(palavra[-i-1])
        
reverse("helson")

print(palavra_invertida)