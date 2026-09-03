import pyautogui as py
from time import sleep
from datetime import date

def hoje():
  return date.today().strftime(f"%d/%m/%y")

def criar_mensagem():
  return input('Informe a mensagem do GIT: ')

def abrir_terminal():
  py.press('win')
  py.write('cmd')
  py.press('enter')

def abrir_pasta():
  comando = r'cd C:\Users\ALUNO\Thiago\desenvolvedor_python_qua.544.003'
  py.write(comando)
  py.press('enter')

def comandos_git():
  py.write('git add .')
  py.press('enter')
  py.write(f'git commit -m " Automação - Data: {hoje()}"')
  py.press('enter')
  py.write('git push')
  py.press('enter')  

def main ():
  py.PAUSE = 0.7
  abrir_terminal()
  abrir_pasta()
  comandos_git()



if __name__ == '__main__':
  main()