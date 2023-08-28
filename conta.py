class Conta:
    def __init__(self, numero:int, saldo:float):
        self.numero = numero
        self.limite = 100
        self.extrato = []
        self.saldo = saldo + self.limite

    def getNumero(self):
        return self.numero

    def getSaldo(self):
        return self.saldo

    def getLimite(self):
        return self.limite

    def sacar(self, valor: float):
        if valor > 0 and valor <= self.saldo:
            self.saldo -=valor
            self.extrato.append("- Saldo")
            return True
        else:
            return False

    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
            self.extrato.append("+ Depositar")
            return True
        else:
            return False

    def transferir(self, destino, valor:float):
        if valor > 0:
            if self.saldo >= valor:
                self.sacar(valor)
                destino.depositar(valor)
                self.extrato.append("- Transferência")
                print("Transferência realizada com sucesso!")
            else:
                return True
        else:
            return False

    def verExtrato(self):
        if len(self.extrato) > 0:
            return self.extrato
        else:
            return None