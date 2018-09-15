from flask import Flask
app = Flask(__name__)

@app.route('/')
def entra():
    return 'huelladigital' 
@app.route('/hola')
def hola():
    return 'hola' 
@app.route('/metio/<nombre>')
def metio(nombre):
    return 'inserto %s'% nombre 

if __name__ == '__main__':
  app.run()
