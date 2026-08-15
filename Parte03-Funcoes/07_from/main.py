from modulo import limpar, somar, subtrair, lerInteiro

def main():
  limpar()
  x = lerInteiro('Numero X: ')
  y = lerInteiro('Numero Y: ')
  print(f'A soma de X e Y é: {somar(x,y)}')
  print(f'A subtração de X e Y é: {subtrair(x,y)}')

if __name__ == '__main__':
  main()