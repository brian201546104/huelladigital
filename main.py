from flask import Flask
app = Flask(__name__)

def get_huella(url='https://huelladigital.azurewebsites.net/',offset=0):
  args={'offset':offset} if offset else{}
  print(args)

if __name__ == '__main__':
  app.run()
