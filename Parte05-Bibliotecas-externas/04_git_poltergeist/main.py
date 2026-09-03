from datetime import date
from time import sleep
import pyautogui as py
#NOTE - Gerar o executavel:
# pyinstaller --onefile --name "GitPush Poltergeist v1.0" --icon "icon/ghost.ico" main.py
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
  py.write(f'git commit -m " Aula do Dia: {hoje()}"')
  py.press('enter')
  py.write('git push')
  py.press('enter')  

def fechar_cmd():
  sleep(3)
  py.write('exit')
  py.press('enter')  

def main ():
  py.PAUSE = 0.7
  abrir_terminal()
  abrir_pasta()
  comandos_git()
  py.alert(text='Programa realizado com Sucesso!', button='Finalizar')
  fechar_cmd()



if __name__ == '__main__':
  main()