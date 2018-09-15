from flask import Flask
app = Flask(__name__)

@app.route('/')
def entra(contra):
    return 'huelladigital' 


if __name__ == '__main__':
  app.run()
