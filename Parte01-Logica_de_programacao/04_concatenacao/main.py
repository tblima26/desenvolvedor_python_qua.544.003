nome = input('Nome: ')
tel = input('Telefone:')

# NOTE - Modo 1: Utilizando virgulas
print('Olá ',nome,'. Telefone: ',tel)

# NOTE - Modo 2: Utilizando +
print('Adição: '+nome.lower()+'. Telefone: '+tel)

# NOTE - Modo 3: Utilizando formatação
print("Formatando: {}. Telefone: {}".format(nome.capitalize(), tel))

# NOTE - Modo 4: Utilizando formatação
print(f"Formatando: {nome.upper()}. Telefone: {tel}")