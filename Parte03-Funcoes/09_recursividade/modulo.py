import os

def limpar():
  os.system('cls' if os.name=='nt' else "clear")

def lerFloat(msg):
  return float(input(msg).replace(',','.'))

def lerInteiro(msg):
  return int(input(msg))

def fatorial(n):
  if n ==0:
    return 1
  return 1 if n==1 else  n * fatorial(n-1)