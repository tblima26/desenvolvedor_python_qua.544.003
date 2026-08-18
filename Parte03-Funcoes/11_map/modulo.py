import os

def limpar():
  os.system('cls' if os.name=='nt' else "clear")

def lerFloat(msg):
  return float(input(msg).replace(',','.'))

def lerInteiro(msg):
  return int(input(msg))

def lerString(msg):
  return input(msg).strip().title()

def fibonacci_recursivo(n):
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)