from flask import Flask
app = Flask(__name__)

@app.route('/')
def huella(url='https://huelladigital.azurewebsites.net/',offset=0):
  args={'offset':offset} if offset else{}
  return args

if __name__ == '__main__':
  app.run()
