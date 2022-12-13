import random

class Conta():
    def __init__(self, num_conta):
        self.numero = num_conta
        self.saldo = 0
    
    def deposit(self, valor):
        self.saldo = self.saldo + valor  - (valor * 0.001)
    
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            return True
        else:
            return False
class Poupanca(Conta):
    def __init__(self, num_conta, percentual):
        self.percentual = percentual
        super().__init__(num_conta)
    
    def render(self):
        self.saldo = self.saldo + self.saldo * (0.01 * self.percentual)
        
        
class ContaBonificada(Conta):
    def __init__(self, num_conta):
        super().__init__(num_conta)
        self.bonus = 0
        
    def deposit(self, valor):
        self.bonus += valor*0.0001
        super().deposit(valor)

    def render_bonus(self):
        self.saldo = self.saldo + self.bonus
        self.bonus = 0
class Banco():
    def __init__(self, nome_banco):
        self.nome = nome_banco
        self.contas = []
        
    def getNome(self):
        return self.nome
        
    def criar_conta(self):
        num = random.randint(0, 1000)
        conta_corrente = Conta(num)
        self.contas.append(conta_corrente)
        self.saldo = 0
        return num
    
    def criar_poupanca(self, percentual):
        num = random.randint(0, 1000)
        conta_poupanca = Poupanca(num, percentual)
        self.contas.append(conta_poupanca)
        self.saldo = 0
        return num
    
    def criar_conta_bonificada(self):
        num = random.randint(0, 1000)
        conta_bonificada = ContaBonificada(num)
        self.contas.append(conta_bonificada)
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
                return conta.saque(valor)
    
    def render_poupanca(self, num_conta):
        for conta in self.contas:
            if(conta.numero) == num_conta and isinstance(conta, Poupanca):
                conta.render()
                return True
        return False

    def render_bonus(self, num_conta):
        for conta in self.contas:
            if(conta.numero) == num_conta and isinstance(conta, ContaBonificada):
                conta.render_bonus()
                return True
        return False