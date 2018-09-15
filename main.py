from flask import Flask
app = Flask(__name__)


@app.route('/<nombre>')
def saludo(nombre):
    return 'Hola ' + nombre + '!!!'

if __name__ == '__main__':
  app.run()
