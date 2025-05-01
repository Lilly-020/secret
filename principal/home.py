from principal import app
from flask import render_template

#Cria uma rota para a página inicial
@app.route('/')
def home():
    return render_template('home.html')