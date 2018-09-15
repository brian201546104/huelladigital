from flask import Flask
app = Flask(__name__)

@app.route('/')
def entra():
    return 'huelladigital' 
@app.route('/hola')
def hola():
    return 'hola' 
@app.route('/<nombre>')
def saludo(nombre):
    return 'Hola ' + nombre + '!!!'

if __name__ == '__main__':
  app.run()
