frutas = ['Maça','Abacaxi','Morango','Maracujá','Mixirica']
pessoa = { "id":1,"nome":"Pedro"}
#NOTE - Usando enumerador
for i,fruta in enumerate(frutas, start=1):
  print(f'Fruta {i}: {fruta}')
print(pessoa["nome"])

#NOTE - Usando Set
pessoas = [
    {"nome": "Ana", "idade": 25, "altura": 1.68},
    {"nome": "Bruno", "idade": 30, "altura": 1.75},
    {"nome": "Carla", "idade": 22, "altura": 1.60}
]

# Lista com 3 pessoas cadastradas
pessoas = [
    {"nome": "Ana", "idade": 25, "altura": 1.68},
    {"nome": "Bruno", "idade": 30, "altura": 1.75},
    {"nome": "Carla", "idade": 22, "altura": 1.60}
]

print("--- 1 pessoa ---")
print(pessoas[0])

print("\n--- 2 pessoas ---")
print(pessoas[0])
print(pessoas[1])

print("\n--- Todas as pessoas ---")
for pessoa in pessoas:
    print(pessoa)

print("\n--- Apenas o nome de uma pessoa (Ana) ---")
print(pessoas[0]["nome"])

print("\n--- Apenas a idade de outra pessoa (Bruno) ---")
print(pessoas[1]["idade"])