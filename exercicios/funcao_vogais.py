vogais = ['a','e','i','o','u']
num_vogais = []

def quant_vogais(palavra):
    for i in palavra:
        if i.lower() in vogais:
            
            num_vogais.append(i)
            
quant_vogais('anderson')            

print("A quantidade de vogais é {}".format(len(num_vogais)))