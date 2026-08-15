import os
import math

def limpar():
  os.system('cls' if os.name=='nt' else "clear")

def lerFloat(msg):
  return float(input(msg).replace(',','.'))

def lerInteiro(msg):
  return int(input(msg))  

def equacaoSegundoGrau(a,b,c):
  if a == 0:
    yield 'Equanção de Primeiro Grau.'
    return
  delta = math.pow(b,2) -(4*a*c)
  if delta < 0:
    yield 'Equação não possui raizes reais.'
    return
  if delta == 0:
    x = -b / (2 * a)
    yield x
  if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    yield x1
    yield x2