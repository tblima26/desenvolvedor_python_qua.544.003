''' 
#NOTE - Versão Antiga
--> os.system('cls' if os.name == 'nt' else 'clear')
'''

#NOTE - Importação de bibliotecas
import os
import subprocess

while True:
  #SECTION - Limpeza de tela
  resultado = subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

  if resultado.returncode == 0:
    print("Tela limpa com sucesso!")

  #SECTION - Entrada de Dados
  nome = input('Name: ').strip().title()
  idade = int(input('Idade: '))
  email = input('Email:').strip().lower()
  subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
  
  #SECTION - Views do Programa
  print(f'Nome: {nome}.')
  print(f'Idade: {idade}.')
  print(f'Email: {email}.')
  print('---------------------')
  print('1 - Novos Dados')
  print('2 - Sair')
  option = int(input('Opção: '))
  match option:
    case 1:
      continue
    case 2:
      print('Finalizando programa.')
      break
    case _:
      print('Opção invalida. O programa')
  