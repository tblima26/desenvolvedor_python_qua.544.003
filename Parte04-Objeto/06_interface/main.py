import os
import datetime
from datetime import date
from modelo import Conta

def limpar():
  os.system('cls' if os.name == 'nt' else 'clear')

def hoje():
  return date.today().strftime("%d/%m/%y")

def agora():
  return datetime.datetime.now().strftime("%H:%M:%S")

def menu():
  print("\n====================")
  print("    MENU BANCÁRIO   ")
  print("====================")
  print("1. Consultar Conta")
  print("2. Fazer Depósito")
  print("3. Fazer Saque")
  print("0. Sair")
  return int(input("Escolha uma opção: "))
  
def main():
  limpar()
  cc = Conta(
    titular="Carlos Eduardo",
    cpf="111.222.333-44",
    agencia="0001",
    conta="98765-4",
    saldo=1000.0
  )
  print(f'Conta criada no dia {hoje()} as {agora()}')
  
  while True:
    match menu():
      case 1:
        limpar()
        print("\n--- CONSULTA ---")
        cc.consultarConta()        
        print(f"Data da consulta: {hoje()}")
        print(f"Hora da consulta: {agora()}")
        input()
        continue
      case 2:
        limpar()
        print("\n--- DEPÓSITO ---")
        valor = float(input("Digite o valor do depósito: R$ "))
        if valor>0:
          cc.fazerDeposito(valor)
          print('Valor depositado com sucesso.')
          print(f'Data:{hoje()} - Hora: {agora()}')
        else:
          print('Valor não pode ser depositado.')  
        continue
      case 3:
        limpar()
        print("\n--- SAQUE ---")
        valor = float(input("Digite o valor do saque: R$ "))
        if valor >=0:
          if valor <= cc.saldo:
            cc.fazerSaque(valor)
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            print(f'Data:{hoje()} - Hora: {agora()}')
          else:
            print(f'Saldo insuficiente')
        else:
            print('Valor não pode ser sacado')
        continue
      case 0:
          limpar()
          print("\nSaindo do sistema... Até logo!")
          break          
      case _:
          print("\n[Erro] Opção inválida!")
if __name__ == '__main__':
  main()