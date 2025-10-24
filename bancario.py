class Cliente:
    def __init__(self,nome,cpf,data_nascimento,endereco,):
        self.nome=nome
        self.cpf=cpf
        self.data_nascimento=data_nascimento
        self.endereco=endereco

class Conta(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco,saldo,senha):
        super().__init__(nome, cpf, data_nascimento, endereco)
        self.saldo=saldo
        self.__senha=senha

    def abrir_conta(self):
        return f"Conta de {self.nome} aberta com sucesso!"
    

    def depositar(self,valor):
        self.saldo+=valor
        return self.saldo
    
    def sacar(self,valor):
        if valor>self.saldo:
            return "Saldo invalido"
        else:
            self.saldo-=valor
            return self.saldo
        
    def ver_saldo(self):
        return self.saldo

class Conta_Poupanca(Conta):
    def __init__(self, nome, cpf, data_nascimento, endereco,saldo,rendimento):
        super().__init__(nome, cpf, data_nascimento, endereco,saldo)
        self.rendimento=rendimento

    def aplicar_rendimento(self):
        self.saldo+=self.saldo*self.rendimento
        return self.saldo
class Conta_Corrente(Conta):
    def __init__(self, nome, cpf, data_nascimento, endereco,saldo,limite):
        super().__init__(nome, cpf, data_nascimento, endereco,saldo)
        self.limite=limite

    def sacar(self,valor):
        if valor>self.saldo + self.limite:
            return "Saldo invalido"
        else:
            self.saldo-=valor
            return self.saldo
class banco:
    def __init__(self,nome,agencia,contas):
        self.nome=nome
        self.agencia=agencia
        self.contas=contas

    def adicionar_conta(self,conta):
        self.contas.append(conta)   

    def remover_conta(self,conta):
        self.contas.remove(conta)
        
    def listar_contas(self):
         return self.contas
    
    def buscar_conta(self,cpf):
        for conta in self.contas:
            if conta.cpf==cpf:
                return conta
        return "Conta nao encontrada"
    

        