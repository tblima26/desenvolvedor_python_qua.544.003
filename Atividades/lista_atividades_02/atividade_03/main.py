'''
#TODO - Atividade 03
# Crie um programa que receba o nome de um aluno e três notas. 
# O programa deve calcular a média do aluno e informar se ele está aprovado ou reprovado.
# Além disso, os dados devem ser salvos em um arquivo JSON. 
# Ao final do cadastro, o usuário deverá ter a opção de escolher se deseja inserir as notas de outro aluno
# As notas também deverão ser gravadas no mesmo arquivo JSON.
'''
import os
import json
#SECTION - Funções
def limpaTela():
  os.system('cls' if os.name =='nt' else 'clear')
def criaPasta():
  os.makedirs('atividade_03/banco',exist_ok=True)

def lerAluno():
  print("\n--- SISTEMA DE NOTAS ---")
  nome = input('Aluno: ')
  n1 = float(input('Nota 1: '))
  n2 = float(input('Nota 2: '))
  n3 = float(input('Nota 3: '))
  aluno = {
    "nome":nome,
    "n1":n1,
    "n2":n2,
    "n3":n3,
  }
  return aluno

def calculaMédia(aluno):
  resultado = (aluno['n1'] + aluno['n2'] + aluno['n3'] ) /3
  return resultado

def menu():
  print("\n--- SISTEMA DE NOTAS ---")
  print("\nDeseja Continuar")
  print("1 - Sim")
  print("2 - Não")
  opcao = int(input("\nOpção: "))
  return opcao

def salvaAluno(aluno,media):
  situacao = 'Aprovado' if media >= 6.0 else 'Reprovado'

  alunoJson = {
    "nome": aluno["nome"],
    "n1": aluno["n1"],
    "n2": aluno["n2"],
    "n3": aluno["n3"],
    "media": round(media,2),
    "situacao": situacao,
  }
  alunos = []
  if os.path.exists('atividade_03/banco/alunos.json'):
    with open(f'atividade_03/banco/alunos.json','r',encoding='utf-8') as f:
      alunos = json.load(f)
  alunos.append(alunoJson)
  with open(f'atividade_03/banco/alunos.json','w',encoding='utf-8') as f:
    json.dump(alunos,f,indent=4, ensure_ascii=False)


#SECTION - Main

while True:
  limpaTela()
  aluno = lerAluno()
  media = calculaMédia(aluno)
  criaPasta()
  salvaAluno(aluno, media)
  option = menu()
  if option == 1:
    continue
  else:
    break

