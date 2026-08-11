import json
import os

#SECTION - Funções
def limpaTela():
  os.system('cls' if os.name=='nt' else 'clear')

def listarArquivos():
  print(f"{'=' * 20}")
  print(" ARQUIVOS CADASTRADOS ")
  print(f"{'=' * 20}")
  if os.path.exists('23_json/banco'):
      arquivos = [f for f in os.listdir('23_json/banco') if f.endswith('.json')]   
      if arquivos:
          for i, arq in enumerate(arquivos, 1):
              nome_limpo = arq.replace('.json', '')
              print(f"{i} - {nome_limpo}")
          return arquivos
      else:
          print("Nenhum arquivo JSON encontrado.")
  else:
      print("A pasta de banco de dados ainda não existe.")

def menu():
  print("====================")
  print("        MENU        ")
  print("====================")
  print("1 - Gravar novo arquivo JSON")
  print("2 - Gravar em arquivo existente")
  print("3 - Ler arquivo")
  print("4 - Sair do programa")
  print("====================")
  opcao = int(input("Opção: "))
  return opcao

def lerUsuario():
  usuario = {}
  usuario['nome']= input(f'\nNome: ').capitalize().strip()
  usuario['email']= input(f'\nEmail: ').strip().lower()
  return usuario

usuarios = []
abrir=''
os.makedirs('23_json/banco', exist_ok=True)
while True:
  limpaTela()
  opcao = menu()
  limpaTela()
  if (opcao ==1 or opcao == 2):
    usuarios.append(lerUsuario())
    match opcao:
      case 1:
        limpaTela()
        arquivo1 = input("Arquivo: ")
        with open(f'23_json/banco/{arquivo1}.json','w',encoding="utf-8") as f:
          json.dump(usuarios,f)
      case 2:
        limpaTela()
        listarArquivos()
        abrir = input("\nArquivo: ")
        if abrir:
          with open(f'23_json/banco/{abrir}.json','w',encoding="utf-8") as f:
            json.dump(usuarios,f)
  else:
    match opcao:
      case 3:
        limpaTela()
        listarArquivos()
        abrir = input(f'\n\nNome do Arquivo: ')
        with open(f'23_json/banco/{abrir}.json','r',encoding="utf-8") as f:
          usuarios = json.load(f)
        for usuario in usuarios:
          for chave, valor in usuario.items():
            print(f'{chave.capitalize()}: {valor}')
        input('\nAperte para continuar...')

      case 4:
        break
      case _:
        input('\nOpção invalida. \n\nAperte para continuar...')