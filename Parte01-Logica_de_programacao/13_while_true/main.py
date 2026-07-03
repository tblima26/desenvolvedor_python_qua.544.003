try:
  while True:
    nome = input('Nome do pagante: ').strip().title()
    idade = int(input('Idade :'))
    altura = float(input('Altura:').replace(',','.'))

    if idade >= 12 and altura >= 1.25:
      print(f'Entrada de {nome} está liberada.')
    else:
      print(f'Entrada de {nome} está proibida.')
    print(f'1 - Novo pagante')
    print(f'2 - Encerrar o programa')
    opcao = int(input('Opcao: '))

    match opcao:
      case 1:
        continue
      case 2:
        print('Programa encerrado')      
        break
      case _:
        print('Opção invalida.')
        continue
except:
  print('Erro durante a execução.')