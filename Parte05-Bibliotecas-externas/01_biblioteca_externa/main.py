from deep_translator import GoogleTranslator
import os

def limpar():
  os.system('cls' if os.name == 'nt' else 'clear')

def traduzir(texto):
  tradutor = GoogleTranslator(source='auto', target='pt')
  return tradutor.translate(texto)

def menu():
  print("\n--- MENU DE TRADUÇÃO ---")
  print("1. Informar um texto para ser traduzido")
  print("2. Sair do programa")
  opcao = input("Escolha uma opção: ")
  return int(opcao)
   

def main():
  limpar()
  while True:
    opcao = menu()
    if opcao == 2:
      break
    elif opcao== 1:
      limpar()
      texto = input('\nTexto a ser traduzido: ')
      print(traduzir(texto))
      continue
    else:
      print('Opção invalida.')
      continue

if __name__ == "__main__":
    main()