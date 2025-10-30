from bancario import Cliente,Conta,Conta_Poupanca,Conta_Corrente
from bancobanc import Banco

def menu(cliente):
    while True:
        print('''👩‍💻🏛️💸💵💵--- BANCO INTER ---👩‍💻🏛️💸💵💵''')
        print("""
        ======= MENU =======
        1 - Ver saldo
        2 - Excluir Cliente
        3 - Depositar
        4 - Sacar
        5 - Criar Conta Poupanca
        6 - Criar Conta Corrente
        7 - Listar Contas
        8 - Sair
        ====================
        """)
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            print(f"Seu saldo atual é: R$ {cliente.ver_saldo():.2f}")

        elif opcao == "2":
            valor = float(input("Digite o valor a depositar: R$ "))
            cliente.depositar(valor)
            print(f"Deposito de R$ {valor:.2f} realizado com sucesso!")

        elif opcao == "3":
            valor = float(input("Digite o valor a sacar: R$ "))
            resultado = cliente.sacar(valor)
            if resultado == "Saldo invalido":
                print("Seu saldo é insuficiente para saque.")

            else:
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

        elif opcao == "4":
            nome = input("Por Favor informe seu nome: ")
            cpf = input("Informe seu CPF: ")
            data_nascimento = input("Informe sua data de nascimento: ")
            endereco = input("Informe seu endereco: ")
            saldo = float(input("Informe o saldo inicial: R$ "))
            conta = Conta_Poupanca(nome, cpf, data_nascimento, endereco, saldo)
            print("Sua conta Poupança foi criada com sucesso!")

        elif opcao == "5":
            nome = input("Por Favor informe seu nome: ")
            cpf = input("Informe seu CPF: ")
            data_nascimento = input("Informe sua data de nascimento: ")
            endereco = input("Informe seu endereco: ")
            saldo = float(input("Informe o saldo inicial: R$ "))
            limite = float(input("Informe o limite da conta corrente: R$ "))
            conta = Conta_Corrente(nome, cpf, data_nascimento, endereco, saldo, limite)
            print("Sua conta Corrente foi criada com sucesso!")

        elif opcao == "6":
            contas = [cliente]  # Exemplo de lista de contas, pode ser substituída por uma lista real
            Banco.listar_contas(contas)

        elif opcao == "7":
            print("Saindo do Banco Inter...")
            break

        else:
            print("Opção não encontrada! gostaria de tentar novamente?")

if __name__ == "__main__":
    cliente1 = Conta_Corrente("Joao Silva", "123.456.789-00", "01/01/1990", "Rua A, 123", 1000.0, 500.0)
    print(cliente1.abrir_conta())
    menu(cliente1)

