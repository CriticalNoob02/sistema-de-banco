## Importações;
from Atv_13 import GerarContaPessoal, CriandoTipoConta, Operações, Loguin, PegandoID, Banco
import sqlite3

## Váriaveis;
entrada = True

## Banco de Dados;
conexão = sqlite3.connect("CadastroClientes.db")
cursor = conexão.cursor()

while entrada:
    print("################################# Bem Vindo ao Caixa Eletrônico #################################")
    print("")

    ## Entrando na Conta;
    pergunta1 = int(input("Você já possui conta bancária? (1-S / 2-N) "))
    match pergunta1:
        case 1:
            print("")
            print("Vamos Acessar sua conta então...")
            print("")
            conta1 = Banco()
            Loguin(conta1)
            id = PegandoID(conta1)
        case 2:
            print("")
            print("Vamos Criar sua conta então...")
            print("")
            conta1 = GerarContaPessoal()
            id = PegandoID(conta1)
            CriandoTipoConta(conta1, id)


    Operações(conta1)