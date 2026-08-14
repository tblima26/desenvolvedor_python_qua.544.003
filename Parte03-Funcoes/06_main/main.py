import modulo as m

def main():
  m.limpar()
  nome = m.lerString('Nome: ')
  idade = m.lerInteiro('Idade: ')
  print(f'{nome} {m.maiorIdade(idade)}')

if __name__ == '__main__':
  main()

