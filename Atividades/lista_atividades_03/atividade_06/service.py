import os

def limpar():
  os.system('cls' if os.name=='nt' else "clear")

def lerFloat(msg):
  return float(input(msg).replace(',','.').strip())

def lerInteiro(msg):
  return int(input(msg).strip())

def lerString(msg):
  return input(msg).strip().title()