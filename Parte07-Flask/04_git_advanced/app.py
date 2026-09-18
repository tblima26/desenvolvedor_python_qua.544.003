from flask import Flask, render_template, request
from datetime import date
import pyautogui as py
import webview
import sys
import os

if getattr(sys, 'frozen', False):
  template_folder = os.path.join(sys._MEIPASS, 'templates')
  static_folder = os.path.join(sys._MEIPASS, 'static')
  app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
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
    py.write('git push'); py.press('enter')
    py.alert("Continuar....")
    py.sleep(3)
    py.write('exit')
    py.press('enter')
  else:
    msg = "Repositorio Invalido"
    py.alert(msg)
  return render_template('index.html')

if __name__ == "__main__":
  # app.run(debug=True)
  window = webview.create_window(
    title="Git Advanced",
    url=app,
    width=600,
    height=600,
  )
  webview.start(debug=False)

  #NOTE - Comando para gerar o build da aplicação:
  # pyinstaller --onefile --noconsole --name "Git Advanced" --icon "static/icons/ghost.ico" --add-data "templates;templates" --add-data "static;static" app.py