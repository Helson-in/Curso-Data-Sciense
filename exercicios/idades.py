soma_idades = 0
lista_idade = []
idade = int(input("Digite a idade: "))

while idade >= 0:
    lista_idade.append(idade)
    idade = int(input("Digite a idade: "))

print(lista_idade)

for i in lista_idade:
    soma_idades +=  i
    print(soma_idades)
    
media = soma_idades / len(lista_idade)

print("A média das idades é {}".format(media))