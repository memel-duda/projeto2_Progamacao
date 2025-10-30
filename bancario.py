import json
class Cliente:
    
    __aquivo="clientes.json"
    def __init__(self,nome,cpf,data_nascimento,endereco,):
        self.nome=nome
        self.cpf=cpf
        self.data_nascimento=data_nascimento
        self.endereco=endereco

    @classmethod
    def carregar_clientes(cls):    
        try:
            with open(cls.__aquivo,"r",encoding="utf-8") as arquivo:
                    clientes=json.load(arquivo)


        except FileNotFoundError:
            with open(cls.__aquivo,"w",encoding="utf-8") as arquivo:
                json.dump([],arquivo)
            return []

    
    def salvar_cliente(self):

        """Salva ou atualizar o Cliente ao json"""

        clientes = self.carregar_clientes()

        # verificar de ja existe cliente com mesmo cpf

        atualizado=False
        for c in clientes: 
            if c["cpf"]==self.cpf:
                c["nome"]=self.nome 
                c["data_nascimento"]=self.data_nascimento 
                c["endereco"]=self.endereco 
                atualizado=True
                break

        if not atualizado:
            novo_cliente={

                "nome":self.nome,
                "cpf":self.cpf,
                "data_nascimento":self.data_nascimento,
                "endereco":self.endereco
            }
            clientes.append(novo_cliente) 

        with open(self.__aquivo,"r",encoding="utf-8") as arquivo:
            json.dump(clientes,arquivo,indent=4)

        return "Cliente atualizado com sucesso!" if atualizado else f"Cliente {self.nome} cadastrado com sucesso!"
            

        @classmethod
        def listar_clientes(cls):
            clientes = cls.carregar_clientes()
            return clientes
                
            
            
    @classmethod
    def excluir_cliente(cls,cpf):

           
            clientes = cls.carregar_clientes()
            clientes_atualizados = [c for c in clientes if c["cpf"] != cpf]

            if len(clientes) == len(clientes_atualizados):
                return f"Cliente com CPF {cpf} não encontrado."
            
            with open(cls.__arquivo, "w", encoding="utf-8") as arquivo:
                json.dump(clientes_atualizados, arquivo, indent=4)
            
            return f"Cliente com CPF {cpf} excluído com sucesso!"
             


class Conta:
    def __init__(self,cliente,saldo,senha,endereco):
        self.cliente=cliente
        self.saldo=saldo
        self.__senha=senha
        self.endereco=endereco

    def abrir_conta(self):
        return f"Conta de {self.cliente.nome} aberta com sucesso"
    

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
        super().__init__(Cliente(nome, cpf, data_nascimento, endereco),saldo,senha=None)
        self.rendimento=rendimento

    def aplicar_rendimento(self):
        self.saldo+=self.saldo*self.rendimento
        return self.saldo
    
class Conta_Corrente(Conta):
    def __init__(self, cliente,saldo,senha,limite,endereco):
        super().__init__(cliente,saldo, senha, endereco)
                         
        self.limite=limite

    def sacar(self,valor):
        if valor>self.saldo + self.limite:
            return "Saldo invalido"
        else:
            self.saldo-=valor
            return self.saldo

    

        