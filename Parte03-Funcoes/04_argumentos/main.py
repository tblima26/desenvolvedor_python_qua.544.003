#NOTE - imports
import os
import math

#NOTE - Funções com Retorno
def limpaTela():
  os.system('cls' if os.name=='nt' else 'clear')

def calculaAreaQuadrado(n1,n2):
  return n1 * n2

def calculaAreaTriangulo(n1,n2):
  return (n1 * n2) /2

def calculaAreaCirculo(raio):
  return math.pow(raio,2) * math.pi

def menu():
  limpaTela()
  print(f'{"=" *25}')
  print(f'--- Calcula Area ---')
  print(f'{"=" *25}')
  print('1- Quadrado')
  print('2- Triangulo')
  print('3- Circulo')
  print('4- Sair')
  opcao = input('Opção: ')

def lerNumero(string):
  return float(input(f'\n{string}: ').replace(',','.'))

#NOTE - Main
while True:
  opcao = menu()
  match opcao:
    case 1:
      limpaTela()
      n1 = lerNumero('Base')
      n2 = lerNumero('Altura')
      print(f'Area do Quadrado: {calculaAreaQuadrado(n1,n2)}')
      continue
    case 2:
      limpaTela()
      n1 = lerNumero('Base')
      n2 = lerNumero('Altura')
      print(f'Area do Triangulo: {calculaAreaTriangulo(n1,n2)}')
      continue
    case 3:
      limpaTela()
      raio = lerNumero('Raio do Circulo')
      print(f'Area do Circulo: {calculaAreaCirculo(raio):.2f}')
      continue
    case 4:
      input('Obrigado por usar a CalcProgramer!')
      break
    case _:
      input('Número invalido. Informe novamente...')
