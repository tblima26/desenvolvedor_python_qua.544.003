import os
from models import Pedido, Calculadora

def limpar():
  os.system('cls' if os.name == 'nt' else 'clear')
def menu():
  print("\n--- CALCULADORA / PEDIDO ---")
  print("1 - Somar")
  print("2 - Subtrair")
  print("3 - Multiplicar")
  print("4 - Dividir")
  opcao = int(input("Escolha uma opção (1-4): "))
  return opcao

def main():
  limpar()
  meu_pedido = Pedido(20, 4)
  opcao_escolhida = menu()
  resultado = meu_pedido.calcular_total(opcao_escolhida)
  input(f"Resultado: {resultado}")

if __name__ == "__main__":
  main()