def calculadora():
    valor = int(input("Primeiro número: "))
    expressao = str(input("Operação(+ - * /):"))
    segundo_valor = int(input("Segundo número: "))
    
    
    if expressao == '+':
        resultado = int(valor) + int(segundo_valor)
        print(resultado)
    elif expressao == '-':
        resultado = int(valor) - int(segundo_valor)
        print(resultado)
    elif expressao == '*':
        resultado = int(valor) * int(segundo_valor)
        print(resultado)
    elif expressao == '/':
        resultado = int(valor) / int(segundo_valor)
        print(resultado)
    else:
        print("Expressão inválida")
    
calculadora()