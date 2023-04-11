class CaixaEletronico:
    def __init__(self):
        self.saldo = 1000

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        print(f"Seu saldo atual é de R${self.saldo:.2f}.")


# Exemplo de uso
caixa = CaixaEletronico()

caixa.consultar_saldo()  # Seu saldo atual é de R$1000.00.

caixa.depositar(500)
caixa.consultar_saldo()  # Seu saldo atual é de R$1500.00.

caixa.sacar(200)
caixa.consultar_saldo()  # Seu saldo atual é de R$1300.00.

caixa.sacar(1500)  # Saldo insuficiente.