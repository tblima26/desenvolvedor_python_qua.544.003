# SECTION Imports
import time 
import os
import subprocess

try:
  n = int(input('Numero:'))
  subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
  while n>=0:
    print(n)
    time.sleep(1)    
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    n-=1
  print('BOOOOOOM 💣💥💥💥')
except Exception as e:
  print(f'Erro: {e}')