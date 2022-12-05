def salario(salario_bruto):
    desconto_inss = salario_bruto * 0.11
    desconto_ir = (salario_bruto - desconto_inss) * 0.15
    
    salario_liquido = salario_bruto - (desconto_inss+desconto_ir)
    print("O salário líquido equivalente é R${}".format(salario_liquido))

salario(5000)