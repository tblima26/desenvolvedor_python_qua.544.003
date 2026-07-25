# TODO 
"""
Crie um programa que roceba nome, peso e altura do usuario ee informe na tela
do seu IMC, o seu diagnosticom com base no valor do IMC. 
"""
import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

nome = input('😐..Nome: ').strip()
peso = float(input(f'💪..Peso: ').replace(',','.'))
altura = float(input(f'🚶‍♀️..Altura: ').replace(',','.'))
limpar()
imc = peso / (altura ** 2)
  
if imc < 18.5:
  resultado = "Abaixo do peso"
elif 18.5 <= imc < 25.0:
  resultado = "Peso normal"
elif 25.0 <= imc < 30.0:
  resultado = "Sobrepeso"
elif 30.0 <= imc < 35.0:
  resultado = "Obesidade Grau I"
elif 35.0 <= imc < 40.0:
  resultado = "Obesidade Grau II"
else:
  resultado = "Obesidade Grau III (Mórbida)"

print(f"Resultdo de: {nome}")
print(f"Seu IMC é {imc:.2f} — Diagnóstico: {resultado}")