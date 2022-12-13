from BancoLib import Banco
    
print("Bem-vindo!")

bancoUfrpe = Banco("UABJ")
print("Menu")

print("0 - Sair: ")
print("1 - Criar uma nova conta: ")
print("2 - Consultar o saldo: ")
print("3 - Depositar: ")
print("4 - Sacar: ")
print("5 - Render Poupança: ")
print("6 - Render Bonûs: ")


escolha = int(input("\nDigite a opção desejada: "))

while escolha > 0:
    if escolha == 1:
        # Criar uma conta
        print("1 - Conta Corrente\n2 - Conta Poupança")
        tipo_conta = int(input("Digite o tipo da conta: "))
        # Criando a conta de acordo com a escolha do usuário
        if tipo_conta == 1:
            num_conta = bancoUfrpe.criar_conta()
        else:
            percentual_poupanca = float(input("Digite o percentual da conta: "))
            num_conta = bancoUfrpe.criar_poupanca(percentual_poupanca)
            
        print("Conta criada: {}".format(num_conta))
        
    elif escolha == 2:
        # Consultar saldo
        num_conta = (int(input("Digite o número da conta: ")))
        saldo = bancoUfrpe.consulta_saldo(num_conta)
        print("Saldo: {}".format(saldo))
        
    elif escolha == 3:
        # Depositar
        num_conta = (int(input("Digite o número da conta: ")))
        valor = (float(input("Digite o valor a ser depositado: ")))
        deposito = bancoUfrpe.depositar(num_conta, valor)
        print("Valor Depositado com Sucesso!")
        
    elif escolha == 4:
        # Sacar
        num_conta = (int(input("Digite o número da conta: ")))
        valor = (float(input("Digite o valor a ser sacado: ")))
        saque = bancoUfrpe.sacar(num_conta, valor)

        if saque:
            print("Saque realizado com sucessor!")
        else:
            print("Saldo insuficiente")
            
    elif escolha == 5:
        # Render Poupança
        num_conta = (int(input("Digite o número da conta: ")))
        resposta = bancoUfrpe.render_poupanca(num_conta)
        if resposta:
            print("Poupança com novo saldo")
        else:
            print("A conta não é poupança ou não existe")
    
    elif escolha == 6:
        # Render Bonûs
        num_conta = (int(input("Digite o número da conta: ")))
        resposta = bancoUfrpe.render_bonus(num_conta)
        if resposta:
            print("Bonûs adicionado a conta")
        else:
            print("A conta inválida")

    escolha = int(input("\nDigite a opção desejada: "))
        