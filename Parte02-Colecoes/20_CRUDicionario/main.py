import os

#SECTION - Funções
def limpaTela():
  os.system('cls' if os.name=='nt' else 'clear')

def menu():
  print("=" * 30)
  print("       CRUDICIONARIO       ")
  print("=" * 30)
  print("[1] Cadastrar nova pessoa")
  print("[2] Listar pessoas") 
  print("[3] Atualizar dados")
  print("[4] Deletar pessoa")
  print("[5] Sair")
  print("=" * 30)

def cadastrar():
    usuario = {}
    usuario["nome"] = input('Nome: ').capitalize().strip()
    usuario["cpf"] = input('CPF: ').capitalize().strip()
    usuario["email"] = input('Email: ').capitalize().strip().lower()
    return usuario

def listar():
    print("\n--- Lista de Usuários ---")
    for usuario in usuarios:
        for chave, valor in usuario.items():
            print(f"{chave.capitalize()}: {valor}")
        print(f"{'-' *40}")

def alterar():
   #TODO - Fazer depois
   return

def remover():
   #TODO - Fazer depois
   return

#SECTION - Main
usuarios = []
while(True):
  limpaTela()
  menu()
  opcao = input('Opção: ')
  limpaTela()
  match opcao:
    case '1':
        usuarios.append(cadastrar())
        continue
    case '2':
        listar()
        continue
    case '3':
        alterar()
        continue
    case '4':
        remover()
        continue
    case '5':
        break
    case _:
        input('\nOpção Invalida.\nContinuar...')
        pass


