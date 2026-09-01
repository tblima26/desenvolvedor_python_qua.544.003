#SECTION - IMPORTS
from dataclasses import dataclass
from abc import ABC, abstractmethod

#SECTION - INTERFACES
class IConta(ABC):
    @abstractmethod
    def consultarDados(self):
        pass
    @abstractmethod
    def gerarExtrato(self):
        pass
    @abstractmethod
    def depositar(self, valor):
        pass
    @abstractmethod
    def sacar(self, valor):
        pass

#SECTION - CLASSE PESSOA
@dataclass
class Pessoa:
    nome: str
    cpf: str

    def __str__(self):
        return f"Nome: {self.nome}\nCpf: {self.cpf}"
    
#SECTION - CLASSES CONTA
@dataclass
class Conta(IConta):
    usuario: Pessoa
    agencia: str
    conta: str
    saldo: float

    def consultarDados(self): # CORRIGIDO: Nome alterado para bater com a interface
        print(f"=== DADOS DA CONTA ===")
        print(f"Titular: {self.usuario.nome}")
        print(f"CPF: {self.usuario.cpf}")
        print(f"Agência: {self.agencia}")
        print(f"Conta: {self.conta}")
        print(f"Saldo Atual: R$ {self.saldo:.2f}")

    def depositar(self, valor): # CORRIGIDO: Nome alterado para bater com a interface
        self.saldo += valor
        return self.saldo

    def sacar(self, valor): # CORRIGIDO: Nome alterado para bater com a interface
        self.saldo -= valor
        return self.saldo

    def gerarExtrato(self): 
        nome_arquivo = f"{self.usuario.nome}.txt"
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo: 
            arquivo.write("=== EXTRATO BANCÁRIO ===\n")
            arquivo.write(f"Titular: {self.usuario.nome}\n")
            arquivo.write(f"CPF: {self.usuario.cpf}\n")
            arquivo.write(f"Agência: {self.agencia}\n")
            arquivo.write(f"Conta: {self.conta}\n")
            arquivo.write(f"Saldo Atual: R$ {self.saldo:.2f}\n")
        print(f"Extrato gerado com sucesso!")