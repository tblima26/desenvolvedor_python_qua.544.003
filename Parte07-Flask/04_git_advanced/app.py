from flask import Flask, render_template, request
import pyautogui as py
from datetime import date

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/comitar', methods=['POST'])
def comitar():
  hoje = date.today().strftime(f"%d/%m/%y")
  repositorio = request.form.get("repositorio","")
  if repositorio:
    py.PAUSE = 1
    py.hotkey('win','r')
    py.write('cmd'); py.press('enter')
    py.write(f'cd {repositorio}'); py.press('enter')
    py.write('git add .'); py.press('enter')
    py.write('git status'); py.press('enter')
    py.write(f'git commit -m "Commit do dia {hoje}"'); py.press('enter')
    py.alert("Continuar....")
    py.write('exit')
    py.press('enter')
  else:
    msg = "Repositorio Invalido"
    py.alert(msg)
  return render_template('index.html')

if __name__ == "__main__":
  app.run(debug=True)