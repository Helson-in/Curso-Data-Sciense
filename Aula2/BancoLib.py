import random

class Conta():
    def __init__(self, num_conta):
        self.numero = num_conta
        self.saldo = 0
    
    def deposit(self, valor):
        self.saldo = self.saldo + valor    
    
    def saque(self, valor):
        self.saldo = self.saldo - valor    
        
class Banco():
    def __init__(self, nome_banco):
        self.nome = nome_banco
        self.contas = []
        
    def getNome(self):
        return self.nome
        
    def criar_conta(self):
        num = random.randint(0, 1000)
        c = Conta(num)
        self.contas.append(c)
        self.saldo = 0
        return num
    
    def consulta_saldo(self, num_conta):
        for conta in self.contas:
            if(conta.numero == num_conta):
                return conta.saldo
        return -1
    
    def depositar(self, num_conta, valor):
        for conta in self.contas:
            if(conta.numero == num_conta):
                conta.deposit(valor)
                
    def sacar(self, num_conta, valor):
        for conta in self.contas:
            if(conta.numero == num_conta):
                conta.saque(valor)
        
print("Bem-vindo!")

bancoUfrpe = Banco("UABJ")
print("Menu")

print("0 - Sair: ")
print("1 - Criar uma nova conta: ")
print("2 - Consultar o saldo: ")
print("3 - Depositar: ")
print("4 - Sacar: ")


escolha = int(input("Digite a opção desejada: "))

while escolha > 0:
    if escolha == 1:
        # Criar uma conta
        num_conta = bancoUfrpe.criar_conta()
        print("Conta criada: {}".format(num_conta))
    elif escolha == 2:
        num_conta = (int(input("Digite o número da conta: ")))
        saldo = bancoUfrpe.consulta_saldo(num_conta)
        print("Saldo: {}".format(saldo))
    elif escolha == 3:
        num_conta = (int(input("Digite o número da conta: ")))
        valor = (float(input("Digite o valor a ser depositado: ")))
        deposito = bancoUfrpe.depositar(num_conta, valor)
        print("Saldo: {}".format(saldo))
        print("Valor Depositado com Sucesso!")
    elif escolha == 4:
        num_conta = (int(input("Digite o número da conta: ")))
        valor = (float(input("Digite o valor a ser sacado: ")))
        saque = bancoUfrpe.sacar(num_conta, valor)
        print("Valor Sacado com Sucesso!")
        
    escolha = int(input("Digite a opção desejada: "))
        