from principal import app, db
from flask import render_template, request
from principal.models.tabelas import Usuario
import re

#Cria uma rota para a página inicial
@app.route('/registrar', methods = ['GET', 'POST'])
def registrar():
    # Verifica se o método da requisição é POST
    if request.method == 'POST':
        nome_usuario = request.form['usuario']
        email = request.form['email']
        senha = request.form['senha']
                         
        #testa se o email esta correto   
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            return render_template('registrar.html', error='Email inválido!')        

        #testa se a senha é valida
        #senha não pode ser vazia
        if senha == '':
            return render_template('registrar.html', error='Senha inválida!')
        #senha não pode ser menor que 6 caracteres
        elif len(senha) < 6:
            return render_template('registrar.html', error='Senha deve ter no mínimo 6 caracteres!')
        #senha não pode ter apenas números
        elif not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$', senha):
            return render_template('registrar.html', error='Senha deve conter letras, números e simbolos!')

        #verifica se o usuario já existe no banco de dados
        if nome_usuario != Usuario.query.filter_by(usuario=nome_usuario).first():
            #se usuario, ele tenta adicionar o usuario ao banco de dados
            try:
                #adicionando novo usuario ao banco de dados
                novo_usuario = Usuario(usuario=nome_usuario, email=email, senha=senha)
                db.session.add(novo_usuario)
                db.session.commit()
            #mas se o usuario já existe, ele retorna um erro 
            except Exception as e:
                db.session.rollback()
                return render_template('registrar.html', error='Usuário já existente!')

        #se tudo estiver correto, ele redireciona para a página de login            
        return render_template('logar.html', usuario=nome_usuario, email=email, senha=senha)

    return render_template('registrar.html')