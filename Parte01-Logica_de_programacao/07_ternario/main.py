#ANCHOR - Variaveis
nome = input('Nome: ').title()
idade = int(input('Idade: '))

#ANCHOR - Ternario
status = "Maior" if idade >= 18 else "Menor"
print(f'(Metodo 1) {nome} é {status.lower()} de idade.')

#REVIEW - Ou fazer em uma linha.
print(f'(Metodo 2) {nome} é maior de idade.' if idade >=18 else f'(Metodo 2) {nome} é menor de idade')