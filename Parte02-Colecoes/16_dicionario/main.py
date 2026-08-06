'''
#LINK - Um dicionário é uma estrutura que armazena dados em formato de chave e valor.
Exemplo: uma agenda, onde você busca um nome pela chave, para ver o telefone um valor). 
Seus itens são mutáveis, mas as chaves devem ser únicas.
Usa-se chaves {} separando a chave do valor com dois pontos (:):
'''
agenda = [
    {"nome": "Ana", "idade": 25},
    {"nome": "Carlos", "idade": 30},
    {"nome": "Mariana", "idade": 22},
]
#LINK - METODO 1

for pessoa in agenda:
  print(f"Nome: {pessoa.get('nome')} - Idade: {pessoa.get('idade')}")

#LINK - METODO 2
for pessoa in agenda:
  for chave in pessoa:
    print(f"{chave.capitalize()}: {pessoa.get(chave)}")
  print("-" * 20)

agenda = {
    1: {"nome": "Ana", "idade": 25},
    2: {"nome": "Carlos", "idade": 30},
    3: {"nome": "Mariana", "idade": 22},
}

#LINK - METODO 1

for numero, pessoa in agenda.items():
  print(f"Registro {numero} -> Nome: {pessoa.get('nome')} - Idade: {pessoa.get('idade')}")
#LINK - METODO 2
for numero, pessoa in agenda.items():
  print(f"Registro {numero}:")
  for chave in pessoa:
    print(f"  {chave.capitalize()}: {pessoa.get(chave)}")
  print("-" * 20)