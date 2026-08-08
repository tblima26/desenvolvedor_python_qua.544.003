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
    print("\n--- Cadastrar Usuários ---")
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
    input('Aperte algo para continuar...')

def alterar():
    print("\n--- Alterar Usuários ---")
    nome = input('Pesquisar o Nome: ').capitalize().strip()
    encontrado = False
    for usuario in usuarios:
        if nome in usuario['nome']:
            encontrado = True
            print(f'{usuario["nome"]}')
            print(f'{usuario["cpf"]}')
            print(f'{usuario["email"]}')
            novo_nome = input(f"Novo nome: ").strip().title()
            novo_cpf = input(f"Novo CPF: ").strip()
            novo_email = input(f"Novo email: ").strip().lower()
            if novo_nome:
                usuario['nome'] = novo_nome
            if novo_cpf:
                usuario['cpf'] = novo_cpf
            if novo_email:
                usuario['email'] = novo_email
            print("\nDados atualizados com sucesso!")
    if not encontrado:
        print(f'{nome} não encontrado.')
        input('\n\nAperte algo para continuar...')


def remover():
    nome = input(f' -- Deletar -- \n\nNome: ').strip().title()
    encontrado = False
    for usuario in usuarios:
      if nome in usuario['nome']:
         encontrado = True
         usuarios.remove(usuario)
         print(f'{nome} deletado com sucesso!')
         input('Aperte algo para continuar...')
    if not encontrado:
      print(f'{nome} não encontrado.')
      input('\n\nAperte algo para continuar...')


#SECTION - Main
usuarios = []
while(True):
  limpaTela()
  menu()
  opcao = input('Opção: ')
  limpaTela()
  match opcao:
    case '1':
        limpaTela()
        usuarios.append(cadastrar())
        continue
    case '2':
        limpaTela()
        listar()
        continue
    case '3':
        limpaTela()
        alterar()
        continue
    case '4':
        limpaTela()
        remover()
        continue
    case '5':
        limpaTela()
        break
    case _:
        input('\nOpção Invalida.\nContinuar...')
        pass


