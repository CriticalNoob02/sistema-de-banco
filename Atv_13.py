import random
from abc import abstractmethod
import sqlite3

## Banco de Dados;
conexão = sqlite3.connect("CadastroClientes.db")
cursor = conexão.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS cadastro("
"id INTEGER PRIMARY KEY AUTOINCREMENT,"
"nome TEXT,"
"idade INT,"
"agencia INT,"
"numero INT,"
"saldo REAL,"
"banco TEXT,"
"conta TEXT"
")")

## Classes Pai;
class Pessoa:
    def __init__(self):
        self.nome = ""
        self.idade = 0

class Conta:
    def __init__(self):
        self.agencia = 0
        self.número = 0
        self.saldo = 0

    def mostrarSaldo(self):
        print("")
        print(f"Seu saldo é : {self.saldo}")

    @abstractmethod
    def sacar(self,Valor):
        pass

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

    def sacar(self, Valor):
        if Valor > (self.saldo+self.limiteEspecial):
            print("Saldo insulficiente!")
        else:
            self.saldo -= Valor
            print(f"Saque Concluido, seu saldo é {self.saldo}")

class ContaPoupança(Conta):
    def __init__(self):
        super().__init__()
    
    def sacar(self, Valor):
        if Valor > self.saldo:
            print("Saldo insulficiente!")
        else:
            self.saldo -= Valor
            print(f"Saque Concluido, seu saldo é {self.saldo}")

## Classe Neta;
class Banco(Cliente,Conta):
    def __init__(self):
        super().__init__()
        self.banco = 0
    
    def sacar(self, Valor):
        return super().sacar(Valor)

    def salvarInformações(self):
        cursor.execute(f"INSERT INTO cadastro(nome, idade, agencia, numero, saldo, banco) VALUES ('{self.nome}', {self.idade}, {self.agencia}, {self.número}, {self.saldo}, '{self.banco}')")
        conexão.commit()

        cursor.execute("SELECT * FROM cadastro")
        for linha in cursor.fetchall():
            print(linha)

    def criarConta(self):
        ## Informações Cliente;
        nome = input("Digite seu Nome: ")
        idade = int(input("Digite sua Idade: "))
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
        self.saldo = 0

    def mostrarConta(self):
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Agência: {self.agencia}")
        print(f"Número da Conta: {self.número}")
        print(f"Seu Saldo: {self.saldo}")
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

    def CarregandoConta(self, nome,idade,agencia,número,saldo,banco,conta):
        self.nome = nome
        self.idade = idade
        self.agencia = agencia
        self.número = número
        self.saldo = saldo
        self.banco = banco
        self.conta = conta

def GerarContaPessoal():
    ## Criando Conta;
    banco1 = Banco()
    banco1.criarConta()
    banco1.mostrarConta()
    banco1.mostrarSaldo()
    banco1.salvarInformações()

    return banco1

def CriandoTipoConta(banco1, id):
    ## Escolhendo tipo da conta;
    conta = int(input("Qual tipo de conta deseja acessar? ( 1 - Corrente/ 2 - Poupança ) "))
    corrente = ContaCorrente()
    poupança = ContaPoupança()
    match conta:
        case 1:
            banco1.conta = corrente
            banco1.conta.addLimite()
            print("")
            print(f"Parabéns, você acabou de ganhar um limite de R${banco1.conta.limiteEspecial} de Cheque Especial.")
            print("")
            conexão.execute(f"UPDATE cadastro SET conta ='corrente' WHERE id ={id}")
            conexão.commit()
        case 2:
            banco1.conta = poupança
            conexão.execute(f"UPDATE cadastro SET conta = 'poupança' WHERE id = {id}")
            conexão.commit()
    
def Operações(banco1):
    ## Sacar ou depositar;
    operação = int(input("Qual a operação desejada? ( 1- Sacar / 2- Depositar ) "))
    valor = int(input("E qual o valor da Operação? "))
    match operação:
        case 1:
            banco1.conta.sacar(valor)
        case 2:
            banco1.depositar(valor)

def Loguin(banco1):
    nomeInput = input("Digite seu nome: ")
    numeroInput = int(input("Digite sua conta: "))
    ## Nome;
    cursor.execute("SELECT nome FROM cadastro WHERE nome = ? AND numero = ?",(nomeInput,numeroInput))
    for linha in cursor.fetchall():
        nome = "".join(linha)
    ## Idade;
    cursor.execute("SELECT idade FROM cadastro WHERE nome = ? AND numero = ?",(nomeInput,numeroInput))
    for linha in cursor.fetchall():
        idade = linha[0]
    ## Agência;
    cursor.execute("SELECT agencia FROM cadastro WHERE nome = ? AND numero = ?",(nomeInput,numeroInput))
    for linha in cursor.fetchall():
        agencia = linha[0]
    ## Número;
    cursor.execute("SELECT numero FROM cadastro WHERE nome = ? AND numero = ?",(nomeInput,numeroInput))
    for linha in cursor.fetchall():
        numero = linha[0]
    ## Saldo;
    cursor.execute("SELECT saldo FROM cadastro WHERE nome = ? AND numero = ?",(nomeInput,numeroInput))
    for linha in cursor.fetchall():
        saldo = linha[0]
    ## Banco;
    cursor.execute("SELECT banco FROM cadastro WHERE nome = ? AND numero = ?",(nomeInput,numeroInput))
    for linha in cursor.fetchall():
        banco = "".join(linha)
    ## Conta;
    cursor.execute("SELECT conta FROM cadastro WHERE nome = ? AND numero = ?",(nomeInput,numeroInput))
    for linha in cursor.fetchall():
        conta = linha
    ## Chamando Função;
    banco1.CarregandoConta(nome,idade,agencia,numero,saldo,banco,conta)
    banco1.mostrarConta()

def PegandoID(banco1):
    conta = banco1.número
    cursor.execute(f"SELECT id FROM cadastro WHERE numero = {conta}")
    for linha in cursor.fetchall():
        id = linha[0]
    return id