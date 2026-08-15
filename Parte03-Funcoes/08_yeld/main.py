import modulo as m

def main():
  m.limpar()
  a= m.lerInteiro('Ler A: ')
  b= m.lerInteiro('Ler B: ')
  c= m.lerInteiro('Ler C: ')
  m.limpar()

  resultado = m.equacaoSegundoGrau(a,b,c)
  for x in resultado:
    print(x)
1
if __name__ == '__main__':
  main()