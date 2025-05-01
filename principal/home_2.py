from principal import app
from flask import render_template, request, redirect, url_for
from principal import db
from principal.models.tabelas import Texto
from flask_login import login_required, current_user

@app.route('/home_2')
def home_2(): 
    posts = Texto.query.order_by(Texto.id.desc()).all() 
    return render_template('home_2.html', posts=posts)

@app.route('/add_text', methods=['GET', 'POST'])
@login_required
def add_text():
    if request.method == 'POST':
        titulo = request.form['titulo']
        texto = request.form['texto']

        if titulo.strip() and texto.strip():
            new_post = Texto(titulo=titulo, texto=texto, usuario_id=current_user.id)
            db.session.add(new_post)
            db.session.commit()

            return redirect(url_for('home_2'))
    
    return render_template('add_text.html')

@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response
