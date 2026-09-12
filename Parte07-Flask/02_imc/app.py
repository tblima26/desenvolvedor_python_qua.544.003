from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/imc", methods = ['GET', 'POST'])
def calcular_imc():
    nome = request.form.get("name","")
    peso = float(request.form.get("weight","0").replace(',','.'))
    altura = float(request.form.get("height","0").replace(',','.'))
    # Conversão simples caso a altura esteja em centímetros
    if altura > 3:
        altura = altura / 100
    # Cálculo do IMC com 2 casas decimais
    imc = round(peso / (altura ** 2), 2)
    # Definindo a mensagem com base no resultado
    if imc < 18.5:
        mensagem = "Você está abaixo do peso ideal."
    elif 18.5 <= imc < 25:
        mensagem = "Parabéns, você está com o peso normal!"
    elif 25 <= imc < 30:
        mensagem = "Você está com sobrepeso (acima do peso ideal)."
    else:
        mensagem = "Você está na faixa de obesidade. Cuide-se!"
    
    return render_template("index.html", name=nome, imc=imc, mensagem=mensagem)


if __name__ == "__main__":
    app.run(debug=True)