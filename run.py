from principal import app, db
from principal import home, logar, registrar, home_2
from principal.models import tabelas 

#Para executar o servidor Flask
if __name__ == '__main__':

    #Cria o banco de dados e as tabelas
    with app.app_context():
        db.create_all()

    app.run(debug=True)