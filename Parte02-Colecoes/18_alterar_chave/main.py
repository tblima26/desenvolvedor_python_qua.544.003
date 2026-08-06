#REVIEW - Metodo 
usuario = {
    "nome": "João",
    "idade": 25,
}

# LINK - Metodo 1

usuario["idade"] = 30
for chave in usuario:
  print(f"{chave.lower()}: {usuario.get(chave)}")