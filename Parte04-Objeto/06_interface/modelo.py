from abc import ABC, abstractmethod

class IConta(ABC):
    @abstractmethod
    def consultarConta(self):
        pass
    
    @abstractmethod
    def fazerDeposito(self, valor):
        pass

    @abstractmethod
    def fazerSaque(self, valor):
        pass


class Conta(IConta):
    def __init__(self, titular, cpf, agencia, conta, saldo):
        self.__titular = titular
        self.__cpf = cpf
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = saldo

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def agencia(self):
        return self.__agencia

    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    @property
    def conta(self):
        return self.__conta

    @conta.setter
    def conta(self, conta):
        self.__conta = conta

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    # O nome aqui precisa ser exatamente 'consultarConta' (igual na interface)
    def consultarConta(self):
        print(f"=== DADOS DA CONTA ===")
        print(f"Titular: {self.__titular}")
        print(f"CPF: {self.__cpf}")
        print(f"Agência: {self.__agencia}")
        print(f"Conta: {self.__conta}")
        print(f"Saldo Atual: R$ {self.__saldo:.2f}")

    def fazerDeposito(self, valor):
        self.__saldo += valor
        return self.__saldo

    def fazerSaque(self, valor):
        self.__saldo -= valor
        return self.__saldo