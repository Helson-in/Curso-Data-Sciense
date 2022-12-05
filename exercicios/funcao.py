def metros_cubicos(comprimento, largura, altura):
    metros_total = comprimento * largura * altura
    print("O valor total em metros cúbicos é {}".format(metros_total))
    
compri = float(input("Digite o comprimento: "))
larg = float(input("Digite o largura: "))
altu = float(input("Digite o altura: "))

metros_cubicos(compri, larg, altu)