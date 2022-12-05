maior = 0
lista_posicao = []


for i in range(1, 6):
    valor = int(input("Digite um valor: "))
    lista_posicao.append(valor)
    if valor >= maior:
        maior = valor
        posicao_maior = len(lista_posicao)
      
menor = maior
for i in lista_posicao:  
    if i <= menor:
        menor = i
        posicao_menor = lista_posicao.index(i) + 1
    

print("O maior valor é {maior} e está na posição {posicao_maior} da lista.\nO menor valor é {menor} e está na posicão {posicao_menor}.".format(
    maior = maior, 
    posicao_maior = posicao_maior, 
    menor = menor,
    posicao_menor = posicao_menor))