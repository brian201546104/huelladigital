from flask import Flask
app = Flask(__name__)
@app.route('/ingrese/<contra>',methods=['GET'])
def seguridad(contra):
    return 'ingreso contraseña' + contra 

if __name__ == '__main__':
  app.run()
