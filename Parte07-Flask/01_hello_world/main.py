from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
  nome = request.form.get("nome","")
  return render_template("index.html", nome=nome)

@app.route('/page2')
def page2():
  return render_template("page2.html")

if __name__ == "__main__":
  app.run(debug=True)