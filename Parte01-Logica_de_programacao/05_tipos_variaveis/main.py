nome = input("Nome: ")
idade = int(input('Idade: '))
altura = float(input('Altura: ').replace(',','.'))
# NOTE - Tipando variaveis

print(f'Nome: {nome.lower().capitalize().split()}')
print(type(nome))
print(f'Idade: {idade}')
print(type(idade))
print(f'Altura: {altura}')
print(type(altura))


