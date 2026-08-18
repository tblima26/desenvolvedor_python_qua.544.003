'''
#TODO - atividade 04
Utilizando o conceito de modulo, crie um modulo com funcoes que façam as seguintes ações:
#SECTION
-Limpa o terminal automaticamente a cada iteração do menu principal.
-Calcula a potência de um número informado pelo usuário elevado a um expoente também informado.
-Calcula a raiz quadrada de um número informado pelo usuário.
-Calcula o volume de um recipiente paralelepípedico através da multiplicação de comprimento, largura e altura.
-Calcula o volume de um recipiente cilíndrico utilizando o raio da base e a altura.
-Exibe um menu interativo onde o usuário pode escolher qual operação deseja executar ou optar por sair do programa a qualquer momento.
'''
import modulo as m

while True:
  option = m.menu()
  match option:
    case 1:
      m.menuHeader()
      x = m.lerInteiro('Base: ')
      y = m.lerInteiro('Expoente: ')
      print(f'Potencia = {m.potencia(x,y)}')
      input('\nPressione Enter para continuar...')
    case 2:
      m.menuHeader()
      x = m.lerInteiro('Raiz do número: ')
      print(f'Raiz = {m.raizQuadrada(x)}')
      input('\nPressione Enter para continuar...')
    case 3:
      m.menuHeader()
      base = m.lerFloat('Base: ')
      largura = m.lerFloat('Largura')
      altura = m.lerFloat('Altura: ')
      result = m.areaRetangulo(base,lagura) * altura
      print(f'Volume do Paralelepipedo: {result}')
      input('\nPressione Enter para continuar...')
    case 4:
      m.menuHeader()
      raio = m.lerFloat('Raio: ')
      altura = m.lerFloat('Altura: ')
      result = m.areaCirculo(raio) * altura
      print(f'Volume do Cilindro: {result}')
      input('\nPressione Enter para continuar...')
    case 5:
      m.menuHeader()
      input(f'\nObrigado por usar nosso programa!\nAperte algo para sair.')
      break
    case _:
      input(f'\nNúmero invalido!\nContinuar...')