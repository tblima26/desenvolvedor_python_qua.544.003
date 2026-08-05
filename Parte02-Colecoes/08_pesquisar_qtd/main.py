paises = [
    "Brasil",
    "Alemanha",
    "Brasil",
    "Itália",
    "Brasil",
    "Uruguai",
    "Brasil",
    "Holanda",
    "França",
    "Brasil",
    "Espanha",
    "Brasil",
    "Inglaterra",
    "Portugal",
    "Holanda",
    "Bélgica",
    "Croácia",
    "Japão"
    "Holanda",
    "Portugal",
    "Alemanha",
    "Espanha",
]
'''
#LINK - Modo 1 - Simples
Objetivo: Mostrar quantas vezes o país escolhido aparece.
'''
pais = input('Pesquisar país: ').strip().title()
qtd = paises.count(pais)
if qtd > 0:
    print(f"{pais} aparece {qtd} vez(es).")
else:
    print("País não encontrado.")

'''
#NOTE - Modo 2 - Complexo
Objetivo: Mostrar apenas os que aparecem mais de uma vez.
'''
for pais in set(paises):
  qtd = paises.count(pais)
  if qtd > 1:
    print(f"{pais}: {qtd} vezes")
