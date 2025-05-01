from principal import app
from flask import render_template, request
from flask_login import login_user
from principal.models.tabelas import Usuario

#Cria uma rota para a página inicial
@app.route('/logar', methods = ['GET', 'POST'])
def logar():
    if request.method == 'POST':
        nome_usuario = request.form['usuario']
        senha = request.form['senha']

        # Verifica se o usuário e a senha estão corretos
        usuario = Usuario.query.filter_by(usuario=nome_usuario, senha=senha).first()
        if usuario:
            login_user(usuario)
            return render_template('home_2.html', usuario=nome_usuario)
        else:
            return render_template('logar.html', error='Usuário ou senha inválidos!')
   
    return render_template('logar.html')