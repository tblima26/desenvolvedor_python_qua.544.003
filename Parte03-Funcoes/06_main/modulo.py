import os

def limpar():
  os.system('cls' if os.name=='nt' else "clear")

def maiorIdade(idade):
  return 'Maior de idade.' if idade >=18 else 'Menor de idade.'

def lerFloat(msg):
  return float(input(msg).replace(',','.'))

def lerInteiro(msg):
  return int(input(msg))

def lerString(msg):
  return input(msg).strip().title()