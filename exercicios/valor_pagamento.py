prestacoes = []

def valor_pagamento(valor_conta, dias):
    if dias > 0:
        valor = valor_conta + (valor_conta * 0.03) + ((valor_conta * 0.01) * dias)
        prestacoes.append(valor)
    else:
        valor = valor_conta
        prestacoes.append(valor)
        

valor_prestacao = float(input("Valor da prestação: "))    
dias_atrasados = float(input("Dias atrasador: "))

while valor_prestacao != 0:
    valor_pagamento(valor_prestacao, dias_atrasados)
    
    valor_prestacao = float(input("Valor da prestação: "))
    if valor_prestacao != 0:
        dias_atrasados = float(input("Dias atrasador: "))
 
print("\nRelatório do dia:")

for i in prestacoes:
    print(prestacoes.index(i)+1, i)

valor_total = sum(prestacoes)
print("Valor total: {}".format(valor_total))
print("Quantidade de prestações: {}".format(len(prestacoes)))
