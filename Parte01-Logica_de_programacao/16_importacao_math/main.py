import math

try:
  while True:
    r = float(input('Raio: ').replace(',','.'))
    area = math.pi * math.pow(r,2)
    #!NOTE - Alternativa --> area = math.pi * r**2
    print(f'Area do Circulo: {area:.2f}')
    print('---------------------------')
    print('1- Novo Calculo')
    print('2- Sair')
    opcao = input('Opcao: ').strip()

    match opcao:
      case '1':
        print("Você escolheu a opção 1. Continuando o menu...")
        continue
              
      case '2':
          print("Saindo do programa...")
          break
          
      case _:
          print('Opção inválida. Tente novamente.') # Primeiro exibe a mensagem
          continue
except Exception as e:
  print(f'🔥 Erro: {e}')