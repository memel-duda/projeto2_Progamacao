import json
class Cliente:
    clientes=[]
    __aquivo="clientes.json"
    def __init__(self,nome,cpf,data_nascimento,endereco,):
        self.nome=nome
        self.cpf=cpf
        self.data_nascimento=data_nascimento
        self.endereco=endereco
        
    try:
       with open(__aquivo,"r",encoding="utf-8") as arquivo:
            clientes=json.load(arquivo)


    except FileNotFoundError:
        with open(__aquivo,"w",encoding="utf-8") as arquivo:
            json.dump([],arquivo)

    
    def salvar_cliente(self):

        """Salva ou atualizar o Cliente ao json"""
        novo_cliente={

            "nome":self.nome,
            "cpf":self.cpf,
            "data_nascimento":self.data_nascimento,
            "endereco":self.endereco
        }

        with open(self.__aquivo,"r",encoding="utf-8") as arquivo:
            clientes=json.load(arquivo)
            clientes.append(novo_cliente)
            
            atualizado=False
            for c in clientes: #percorre a cda clinte já salvo
                if c["cpf"]==self.cpf:# se encontra clinte com o mesmo cpf
                    c["nome"]=self.nome # atualiza o nome
                    c["data_nascimento"]=self.data_nascimento #atualiza a data de nascimento
                    c["endereco"]=self.endereco #atualiza o endereco
                    atualizado=True #marca como atualizado

            if not atualizado:#se não obteve cliente com o mesmo cpf
                clientes.append(novo_cliente) #adiciona novo cliente a lista

        with open(self.__aquivo,"w",encoding="utf-8") as arquivo:
            json.dump(clientes,arquivo,indent=4)
            
            if atualizado:
                return "Cliente atualizado com sucesso!"
            else:
                print(f"Cliente {self.nome} cadastrado com sucesso!")

        @classmethod
        def listar_clientes(cls):
            return cls.clientes
                
            
            
        @classmethod
        def excluir_cliente(cls,cpf):
             
            with open(cls.__aquivo,"r",encoding="utf-8") as arquivo:
                clientes=json.load(arquivo)
                clientes_atualizados=[c for c in clientes if c["cpf"]!=cpf]

            with open(cls.__aquivo,"w",encoding="utf-8") as arquivo:
                json.dump(clientes_atualizados,arquivo,indent=4)
                return f"Cliente com CPF {cpf} excluido com sucesso!"
            
    def cadastrar_cliente(self):
        return self.salvar_cliente()
        print(f"Cliente {self.nome} (CPF: {self.cpf}) cadastrado com sucesso.")
    


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


    

        