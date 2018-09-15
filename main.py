from flask import Flask
app = Flask(__name__)

@app.route('/')
def entra(contra):
    return 'huelladigital' 
@app.route('/hola')
def hola(contra):
    return 'hola' 
@app.route('/saludo/<nombre>')
def saludo(nombre):
    return 'Hola ' + nombre + '!!!'

if __name__ == '__main__':
  app.run()
