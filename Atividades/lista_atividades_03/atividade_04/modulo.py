import os
import math

def limpar():
  os.system('cls' if os.name=='nt' else "clear")

def lerFloat(msg):
  return float(input(msg).replace(',','.'))

def lerInteiro(msg):
  return int(input(msg))

def lerString(msg):
  return input(msg).strip().title()

'''
#SECTION - Funções da atividade
'''

def menuHeader():
  limpar()
  print("========================================")
  print("          MENU DE OPERAÇÕES             ")
  print("========================================")

def menu():
  menuHeader()
  print("1 - Calcular a potência de um número")
  print("2 - Calcular a raiz quadrada de um número")
  print("3 - Calcular o volume de um paralelepípedo")
  print("4 - Calcular o volume de um cilindro")
  print("5 - Sair do programa")
  print("========================================")
  
  opcao = int(input("Escolha uma opção (1 a 5): "))
  return opcao

def potencia (x,y):
  return math.pow(x, y)

def raizQuadrada (x):
  return math.sqrt(x)

def areaRetangulo(base,lagura):
  return base * lagura

def areaCirculo(raio):
  return math.pi * (raio **2)
