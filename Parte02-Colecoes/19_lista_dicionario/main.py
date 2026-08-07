usuarios = [
    {"nome": "Beatriz", "idade": 28, "email": "beatriz28@gmail.com"},
    {"nome": "Carlos", "idade": 34, "email": "carlos.silva@gmail.com"},
    {"nome": "Ana", "idade": 22, "email": "ana.lima@gmail.com"},
    {"nome": "Eduardo", "idade": 41, "email": "eduardo_dev@gmail.com"},
    {"nome": "Mariana", "idade": 29, "email": "mariana.costa@gmail.com"}
]

for usuario in usuarios:
  for chave, valor in usuario.items():
    print(f'{chave.capitalize()}: {valor}')
  print(f'{'-'}*40')