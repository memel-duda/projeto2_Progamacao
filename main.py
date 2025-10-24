from bancario import Cliente,Conta,Conta_Poupanca,Conta_Corrente
from banco import Banco

def menu(cliente):
    while True:
        print('''👩‍💻🏛️💸💵💵--- BANCO INTER ---👩‍💻🏛️💸💵💵''')
        print("""
        ======= MENU =======
        1 - Ver saldo
        2 - Depositar
        3 - Sacar
        4 - Criar Conta Poupanca
        5 - Criar Conta Corrente
        6 - Listar Contas
        7. Sair
        ====================
        """)
        opcao = input("Escolha uma opcao: ")
        if opcao == "1":
            print(f"Seu saldo e: R$ {cliente.ver_saldo():.2f}")
        elif opcao == "2":
            valor = float(input("Digite o valor a depositar: R$ "))
            cliente.depositar(valor)
            print(f"Deposito de R$ {valor:.2f} realizado com sucesso!")
        elif opcao == "3":
            valor = float(input("Digite o valor a sacar: R$ "))
            resultado = cliente.sacar(valor)
            if resultado == "Saldo invalido":
                print("Saldo insuficiente para saque.")
            else:
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

        elif opcao == "4":
            nome = input("Digite seu nome: ")
            cpf = input("Digite seu CPF: ")
            data_nascimento = input("Digite sua data de nascimento: ")
            endereco = input("Digite seu endereco: ")
            saldo = float(input("Digite o saldo inicial: R$ "))
            conta = Conta_Poupanca(nome, cpf, data_nascimento, endereco, saldo)
            print("Sua conta Poupança foi criada com sucesso!")

        elif opcao == "7":
            print("Saindo...")
            break
        else:
            print("Opcao invalida! gostaria de tentar novamente?")

if __name__ == "__main__":
    cliente1 = Conta_Corrente("Joao Silva", "123.456.789-00", "01/01/1990", "Rua A, 123", 1000.0, 500.0)
    print(cliente1.abrir_conta())
    menu(cliente1)

