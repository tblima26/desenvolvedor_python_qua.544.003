"""
Crie um programa que receba o nome e a idade do usuário. Em seguida, o sistema deve apresentar as cinco salas de cinema em cartaz, cada uma com um filme de comédia fictício e sua respectiva classificação indicativa: 
- Sala 1 com As Tranças do Rei Careca (Livre)
- Sala 2 com A Volta dos Que Não Foram (12 anos)
- Sala 3 com Poeira em Alto Mar (14 anos)
- Sala 4 com A Vingança do Frango Assado (16 anos)
- Sala 5 com O Incrível Mistério da Lagoa Seca (18 anos)
O usuário deverá escolher a sala desejada. Se o usuário não tiver a idade mínima permitida para o filme escolhido, o programa deve proibir a entrada e exibir novamente as opções de salas para uma nova seleção. Quando o usuário escolher um filme compatível com sua idade, o programa deve gravar os dados do bilhete em um arquivo de texto e encerrar a execução.
"""
import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
  print("--- CINE COMÉDIA DO ABSURDO ---")
  print("1 - As Tranças do Rei Careca (Livre)")
  print("2 - A Volta dos Que Não Foram (12 anos)")
  print("3 - Poeira em Alto Mar (14 anos)")
  print("4 - A Vingança do Frango Assado (16 anos)")
  print("5 - O Incrível Mistério da Lagoa Seca (18 anos)")
  option = int(input('Opcao: '))
  return option

def exibirBilhete(nome, idade, filme_escolhido):
    print("========================================")
    print("       🎟️ BILHETE EMITIDO! 🎟️           ")
    print("========================================")
    print(f" Cliente: {nome}")
    print(f" Idade:   {idade} anos")
    print(f" Filme:   {filme_escolhido}")
    print("========================================")
    print(" Bom filme e divirta-se!")
    print("========================================\n")

def salvarBilhete(nome, idade, filme_escolhido):
   os.makedirs(f'programa_01-02/bilhetes', exist_ok=True)
   conteudo = (
        "========================================\n"
        "       🎟️ BILHETE EMITIDO! 🎟️           \n"
        "========================================\n"
        f" Cliente: {nome}\n"
        f" Idade:   {idade} anos\n"
        f" Filme:   {filme_escolhido}\n"
        "========================================\n"
        " Bom filme e divirta-se!\n"
        "========================================\n"
    )
   with open(f'programa_01-02/bilhetes/{nome}.txt','w',encoding='utf-8') as f:
        f.write(conteudo)
        input('\n ✔  Arquivo gravado com sucesso! Pressione Enter para continuar...')
        limpar()
   
limpar()
print('--- CINE COMÉDIA DO ABSURDO ---')
nome = input('Nome: ')
idade = int(input('Idade: '))

while True:
  limpar()
  option = menu()
  match option:
    case 1:
        valido = "Sucesso"
        filme_escolhido = "As Tranças do Rei Careca"
    case 2:
        valido = "Sucesso" if idade >= 12 else "Invalido"
        filme_escolhido = "A Volta dos Que Não Foram"
    case 3:
        valido = "Sucesso" if idade >= 14 else "Invalido"
        filme_escolhido = "Poeira em Alto Mar"
    case 4:
        valido = "Sucesso" if idade >= 16 else "Invalido"
        filme_escolhido = "A Vingança do Frango Assado"
    case 5:
        valido = "Sucesso" if idade >= 18 else "Invalido"
        filme_escolhido = "O Incrível Mistério da Lagoa Seca"
    case _:
        input("Filme inexistente. Pressione ENTER para tentar novamente...")
        continue
  if valido == 'Sucesso':
    break
  else:
    input('Idade minima não atingida. Escolha outro filme!')
limpar()
salvarBilhete(nome, idade, filme_escolhido)
exibirBilhete(nome, idade, filme_escolhido)

    