import os

def limpar():
  os.system('cls' if os.name=='nt' else "clear")

def lerFloat(msg):
  return float(input(msg).replace(',','.'))

def lerInteiro(msg):
  return int(input(msg))

def somar(x, y):
  return x + y

def subtrair(x, y):
  return x - y

def multiplicar(x, y):
  return x * y

def dividir(x, y):
  return x / y