import pyjokes
from deep_translator import GoogleTranslator
import os

def limpar():
  os.system('cls' if os.name == 'nt' else 'clear')

def gerar_piada():
  tradutor = GoogleTranslator(source="auto", target="pt")
  piada = pyjokes.get_joke()
  return tradutor.translate(piada)

def menu():
  print("\n--- MENU DE PIADAS ---")
  print("1. Gerar uma nova piada")
  print("2. Sair do programa")
  opcao = input("Escolha uma opção: ")
  return int(opcao)

def main():
  while True:
    limpar()
    opcao = menu()
    if opcao == 2:
      break
    if opcao == 1:
      print("Piada: ")
      print(gerar_piada())
      continue
    else:
      print('Opção invalida')
      continue
    


if __name__ == "__main__":
  main()