#REVIEW - Metodo 
usuario = {
    "nome": "João",
    "idade": 25,
}
chave = input('Chave: ').strip().lower()
if chave in usuario:
  usuario[chave] = input(f'Valor para {chave}').strip()
  for chave,valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}")
else:
  print('Chave não encontrada.')