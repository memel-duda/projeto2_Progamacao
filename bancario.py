import json
class Cliente:
    __aquivo="clientes.json"
    def __init__(self,nome,cpf,data_nascimento,endereco,):
        self.nome=nome
        self.cpf=cpf
        self.data_nascimento=data_nascimento
        self.endereco=endereco

class Conta:
    def __init__(self,cliente,saldo,senha):
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


    

        