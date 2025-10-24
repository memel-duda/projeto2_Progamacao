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
    