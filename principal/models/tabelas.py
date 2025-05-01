from principal import app, db
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from principal import login_manager

#Cria a tabela de usuarios
class Usuario(UserMixin ,db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(Integer, primary_key=True)
    usuario = db.Column(String(60), nullable=False, unique=True)
    email = db.Column(String(120), unique=True, nullable=False)
    senha = db.Column(String(16), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.usuario}>'
    
class Texto(db.Model):
    __tablename__ = 'textos'
    id = db.Column(Integer, primary_key=True)
    titulo = db.Column(String(120), nullable=False)
    texto = db.Column(String(500), nullable=False)
    #topico = db.Column(String(120), nullable=True)
    usuario_id = db.Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    
    usuario = db.relationship('Usuario', backref='textos', lazy=True)

    def __repr__(self):
        return f'<Texto {self.titulo}>'

@login_manager.user_loader
def load_user(usuario_id):
    return Usuario.query.get(int(usuario_id)) 