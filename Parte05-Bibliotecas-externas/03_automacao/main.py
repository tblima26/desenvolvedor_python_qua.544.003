import pyautogui as py 
from time import sleep

def abrir_mozila():
  py.press('win')
  py.write('firefox')
  py.press('enter')

def abrir_youtube():
  site = 'www.youtube.com.br'
  py.write(site)
  py.press('enter')

def pesquisar_video(site):
  py.moveTo(x=1000,y=110,duration=0.5)
  py.click()
  py.hotkey('ctrl', 'a')
  py.write(site)
  py.press('enter')

def main():
  py.PAUSE = 0.7
  abrir_mozila()
  abrir_youtube()
  sleep(3.0)
  pesquisar_video('python')
  pesquisar_video('cristiano')
  pesquisar_video('clash of clas')
  sleep(3.0)
  py.hotkey('alt', 'f4')

if __name__ == '__main__':
  main()