x = float(input('Valor de X: ').replace(',','.'))
y = float(input('Valor de Y: ').replace(',','.'))

print('1- somar')
print('2- subtrair')
print('3- multiplicar')
print('4- dividir')
opcao = int(input('Opção desejada:').strip())

match opcao:
  case 1:
    print(f'Resultado : {x+y}.')
  case 2:
    print(f'Resultado : {x-y}.')
  case 3:
    print(f'Resultado :{x*y}.')
  case 4:
    if y != 0:
      print(f'Resultado : {x/y}.')
    else: 
      print(f'O valor de y não pode ser 0.')
  case _:
    print('Opção invalida.')
  

