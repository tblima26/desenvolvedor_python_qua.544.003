try:
  n = int(input('Numero: '))
  while n >=0:
    print(f'{n}')
    n -=1
except:
  print('Não foi possivel exibir a contagem.')