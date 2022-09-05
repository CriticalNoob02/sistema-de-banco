import random

## Classes Pai;
class Pessoa:
    def __init__(self):
        self.nome = ""
        self.idade = 0

class Conta:
    def __init__(self):
        self.agencia = 0
        self.número = 0
        self.saldo = 10

    def mostrarSaldo(self):
        print("")
        print(f"Seu saldo é : {self.saldo}")

    def sacar(self,Valor):
        self.saldo -= Valor
        print(f"Você acaba de SACAR R${Valor}")

    def depositar(self,Valor):
        self.saldo += Valor
        print(f"Você acaba de DEPOSITAR R${Valor}")

## Classes Filho;
class Cliente(Pessoa):
    def __init__(self):
        super().__init__()
        self.conta = ""

class ContaCorrente(Conta):
    def __init__(self):
        super().__init__()
        self.limiteEspecial = 0
    
    def addLimite(self):
        self.limiteEspecial += random.randint(1000,3000)

class ContaPoupança(Conta):
    def __init__(self):
        super().__init__()

## Classe Neta;
class Banco(Cliente,Conta):
    def __init__(self):
        super().__init__()
        self.banco = 0

    def criarConta(self):
        ## Informações Cliente;
        nome = input("Digite seu Nome: ")
        idade = input("Digite sua Idade: ")
        banco = input("Qual o banco da sua Conta: ")
        ## Gerando Números;
        agenciaL = []
        numeroL = []
        for i in range(1,4):
            num = random.choice(["0","1","2","3","4","5","6","7","8","9"])
            agenciaL.append(num)
        for i in range(1,9):
            num1 = random.choice(["0","1","2","3","4","5","6","7","8","9"])
            numeroL.append(num1)
        ## Convertendo;
        agencia = "".join(agenciaL)
        numero = "".join(numeroL)
        ## Adicionando Informações;
        self.nome = nome
        self.idade = idade
        self.agencia = agencia
        self.número = numero
        self.banco = banco

    def mostrarConta(self):
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Agência: {self.agencia}")
        print(f"Número da Conta: {self.número}")
        print(f"Seu Banco: {self.banco}")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    def verificarConta(self):
        banco = input("Digite o Banco que deseja acessar: ")
        if banco == self.banco:
            verificação = True
            print(f"Seja Bem vindo {self.nome}!")
        else:
            verificação = False
            print(f"Caro(a) {self.nome} você não possui conta no banco desejado.")
        return verificação

    def Conta(self,tipo):
        self.conta = tipo

    def operação(self):
        pass

## Criando Conta;
banco1 = Banco()
banco1.criarConta()
banco1.mostrarConta()
banco1.verificarConta()
banco1.mostrarSaldo()

## Escolhendo tipo da conta;
conta = int(input("Qual tipo de conta deseja acessar? ( 1 - Corrente/ 2 - Poupança ) "))
corrente = ContaCorrente()
poupança = ContaPoupança()
match conta:
    case 1:
        banco1.conta = corrente
    case 2:
        banco1.conta = poupança

## Sacar ou depositar;
operação = int(input("Qual a operação desejada? ( 1- Sacar / 2- Depositar ) "))
valor = int(input("E qual o valor da Operação? "))
print(banco1.limiteEspecial)
match operação:
    case 1:
        pass
    case 2:
        banco1.depositar(valor)