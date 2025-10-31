from bancario import Cliente,Conta,Conta_Poupanca,Conta_Corrente


def main():
    conta = None
    while True:
        print('''--- BANCO INTER ---''')
        print("""
        ======= MENU =======
        1 - Cadastrar Cliente
        2 - Listar Clientes
        3 - Excluir Cliente
        4 - Criar Conta Corrente
        5 - Criar Conta Poupanca
        6 - Depositar
        7 - Sacar
        8 - Ver Saldo
        9 - Sair 
        10 - Abrir Conta
        ====================
        """)
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            nome = input("Por Favor informe seu nome: ")
            cpf = input("Informe seu CPF: ")
            data_nascimento = input("Informe sua data de nascimento: ")
            endereco = input("Informe seu endereco: ")
            cliente = Cliente(nome, cpf, data_nascimento, endereco)
            print(cliente.salvar_cliente())
           

        elif opcao == "2":
            clientes = Cliente.listar_clientes()
            if len(clientes) == 0:
                print("Nenhum cliente cadastrado.")
            else:
                for c in clientes:
                    print(f"Nome: {c['nome']}, CPF: {c['cpf']}, Data de Nascimento: {c['data_nascimento']}, Endereço: {c['endereco']}")
         

        elif opcao == "3":  
            cpf = input("Informe o CPF do cliente que deseja excluir: ")
            resultado = Cliente.excluir_cliente(cpf)
            print(resultado)

        elif opcao == "10":  
            nome = input("Por Favor informe seu nome: ")
            cpf = input("Informe seu CPF: ")
            data_nascimento = input("Informe sua data de nascimento: ")
            endereco = input("Informe seu endereco: ")
            cliente = Cliente(nome, cpf, data_nascimento, endereco)
            conta = Conta(cliente,0,"senha",endereco)
            print(conta.abrir_conta())

        elif opcao == "4":
            nome = input("Nome do Cliente: ")
            cpf = input("CPF: ")
            data_nascimento = input("Data de nascimento: ")
            endereco = input("Endereco: ")
            saldo = float(input("Saldo inicial: R$ "))
            senha = input("Senha para conta corrente: ")
            cliente = Cliente(nome, cpf, data_nascimento, endereco)
            conta = Conta_Corrente(cliente, saldo, senha, limite=0)   
            print(conta.abrir_conta())  
            
            

        elif opcao == "5":
            nome = input("Nome do Cliente: ")
            cpf = input("CPF: ")
            data_nascimento = input("Data de nascimento: ")
            endereco = input("Endereco: ")
            saldo = float(input("Saldo inicial: R$ "))
            rendimento = float(input("Rendimento da conta poupança (%): "))
            senha = input("Senha para conta poupança: ")
            cliente = Cliente(nome, cpf, data_nascimento, endereco)
            conta = Conta_Poupanca(cliente, saldo, senha, rendimento)
            print(conta.abrir_conta()) 
            print("Conta após rendimento: ", conta.aplicar_rendimento())
            
        
        elif opcao == "6":
            if conta:
                valor = float(input("Informe o valor a ser depositado: R$ "))
            
                print("Deposito realizado com sucesso! Novo saldo:", conta.depositar(valor))

            else:
                print("Nenhuma conta criada. Por favor, deseja criar uma conta? ")
           

        elif opcao == "7":
            if conta:
                valor = float(input("Informe o valor a ser sacado: R$ "))
                
                print("Resultado:", conta.sacar(valor))
            else:
                print("Nenhuma conta criada. Por favor, deseja criar uma conta? ")

        elif opcao == "8":
            if conta:
                print("Saldo atual: R$ ", conta.ver_saldo())
            else:
                print("Nenhuma conta antiva. Por favor, deseja criar uma conta? ")

        elif opcao == "9":
            print("Foi um prazer atendê-lo, até a próxima!(Banco Inter)")
            break
        
        
        else:
            print("Opção não encontrada! gostaria de tentar novamente?")

if __name__ == "__main__":
    main()

