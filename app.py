from flask import Flask, render_template
from consultclima import clima

app = Flask(__name__)

@app.route('/')     #este es el index
def indice():
    datos = clima()
    return render_template('index.html',datos=datos)
#esta es la respuesta del servidor

if __name__ == '__main__':  #esto es una pregunta si el es el archivo principal
    app.run()

#export FLASK_APP=app.py 'agregamos una variable de entorno'
#set FLASK_APP=app.py
#flask run