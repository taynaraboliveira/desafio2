from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, nome, telefone, renda_mensal):
        self._primeiro_nome = nome.split(" ")[0]
        self._ultimo_nome = nome.split(" ")[-1]
        self._telefone = telefone
        self._renda_mensal = renda_mensal

    @property
    def nome(self):
        return self._primeiro_nome + " " + self._ultimo_nome

    @nome.setter
    def nome(self, novo_nome):
        if type(novo_nome) != str:
            raise TypeError("Tipo da variável deve ser str")
        self._primeiro_nome = novo_nome.split(" ")[0]
        self._ultimo_nome = novo_nome.split(" ")[-1]

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, novo_tel):
        if type(novo_tel) != str:
            raise TypeError("Tipo da variável deve ser str")
        self._telefone = novo_tel

    @property
    def renda_mensal(self):
        return self._renda_mensal

    @abstractmethod
    def tem_cheque_especial(self):
        pass

class ClienteMulher(Cliente):
    def tem_cheque_especial(self):
        return True

class ClienteHomem(Cliente):
    def tem_cheque_especial(self):
        return False

class ContaCorrente:
    def __init__(self, titular):
        self._saldo = 0.0
        self._operacoes = []
        self._titulares = []
        self.adicionar_titular(titular)

    def adicionar_titular(self, titular):
        self._titulares.append(titular)

    def depositar(self, valor: float):
        self._saldo += valor
        self._operacoes.append(f"Depósito de R$ {valor:.2f}")

    def sacar(self, valor: float):
        if not self._titulares[0].tem_cheque_especial():
            if valor <= self._saldo:
                self._saldo -= valor
                self._operacoes.append(f"Saque de R$ {valor:.2f}")
            else:
                raise ValueError("Saldo Insuficiente")
        elif valor <= self._saldo or (self._saldo - valor) >= self._titulares[0].renda_mensal:
            self._saldo -= valor
            self._operacoes.append(f"Saque de R$ {valor:.2f}")
        else:
            raise ValueError("Saldo Insuficiente")

    @property
    def saldo(self):
        return self._saldo

# Exemplo de uso:
cliente_mulher = ClienteMulher("Taynara Barbosa", "373737", 30000)
cliente_homem = ClienteHomem("Mateus", "97987987898", 1000)
conta1 = ContaCorrente(cliente_mulher)
conta2 = ContaCorrente(cliente_homem)

print(conta1.saldo)
print(conta2.saldo)
print()

valor_saque = input('Quanto você quer sacar: ')
valor_saque = float(valor_saque)

try:
    conta1.sacar(valor_saque)
except ValueError as e:
    print(f'Erro durante a execução: {e}')
    
print(conta1._operacoes)

conta1.depositar(5000.0)
conta2.depositar(50.0)

print(conta1.saldo)
print(conta2.saldo)

conta1.sacar(50000)
conta2.sacar(100.0)

print(conta1.saldo)
print(conta2.saldo)

