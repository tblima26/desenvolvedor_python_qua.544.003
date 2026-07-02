aluno = input('Nome do Aluno: ')
nota = float(input('Nota: ').replace(',','.'))

#STUB - Operador booleano
if nota >=0 and nota <=10:
  if nota>=7:
    print(f'{aluno} está aprovado.')
  elif nota>=5:
    print(f'{aluno} está de recuperação.')
  else:
    print(f'{aluno} está reprovado.')
else :
  print(f'Nota de {aluno} invalida.')

#REVIEW - Operador ternario.
status = 'aprovado' if nota >= 7 else 'recuperação' if nota >= 5 else 'reprovado'
print(f'(Metodo 2) {aluno} está {status}.')