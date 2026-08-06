#REVIEW - Metodo 
usuario = {
    "nome": "João",
    "idade": 25,
}

# LINK - Metodo 1
usuario["telefone"] = "11 988887777"
for chave in usuario:
  print(f"{chave.capitalize()}: {usuario.get(chave)}")