import modulo

modulo.limpaTela()

a = float(input('Informe A: ').replace(',','.'))
b = float(input('Informe B: ').replace(',','.'))
x = modulo.equacao(a,b)
print(f'X = {x}')