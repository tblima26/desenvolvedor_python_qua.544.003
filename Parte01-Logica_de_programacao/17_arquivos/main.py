import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


while True:
  limpar()
  print('1- Gravar arquivo')
  print('2- Ler arquivo')
  print('3- Sair')
  opcao = int(input('Opção: '))
  limpar()
  match opcao:
    case 1:
      text =  input(' 🗨... Texto: ')
      nome_arquivo = input('📂...Nome do Arquivo: ').strip()
      #NOTE - Se usar W, ele sobrescreve. Para adicionar, append, usar a letra 'A'
      with open(f'17_arquivos/arquivos/{nome_arquivo}.txt','w',encoding='utf-8') as f:
        f.write(text)
      input('\n ✔  Arquivo gravado com sucesso! Pressione Enter para continuar...')
      continue
    case 2:
      nome_arquivo = input('🗂 - Nome do Arquivo: ').strip()
      limpar()
      try:

        with open(f'17_arquivos/arquivos/{nome_arquivo}.txt','r',encoding='utf-8') as f:
          text = f.read()
        print(f'🔥🔥 - Arquivo {nome_arquivo}')  
        print(text)
        input('')
      except FileNotFoundError:
        print('Arquivo não encontrado.')
        input('')
        
      continue
    case 3:
      input('Programa finalizado.')
      break
    case _: 
      input('Opçao invalida.')
      continue
  