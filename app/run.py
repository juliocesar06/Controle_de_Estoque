from flask import Flask,render_template,url_for,request,redirect,jsonify
from flask_sqlalchemy import SQLAlchemy
from models import *


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'

db = SQLAlchemy(app)


class  Tecido(db.Model):
    id =  db.Column(db.Integer,primary_key=True,autoincrement=True)
    cor= db.Column(db.String(10))
    qtd_mts= db.Column(db.Float)
    qtd_und= db.Column(db.Integer)
    fornecedor= db.Column(db.String(30))
    tipo = db.Column(db.String(30))


    def __init__(self,cor:str,qtd_mts:float,qtd_und:int,fornecedor:str,tipo:str):
        self.cor = cor
        self.qtd_mts = qtd_mts
        self.qtd_und = qtd_und
        self.fornecedor = fornecedor
        self.tipo = tipo



#inicio
@app.route('/')
def index():
    c = Tecido.query.filter_by(tipo = 'leve')
    indice = 0
    return render_template('/index.html',lista=c,indice=indice)

#adcionar tecido cor ,tipo, qtd
@app.route('/add')
def add():
    for i in range(len(add_tecido)):
        try:
            db.session.add(add_tecido[i])
            db.session.commit()
        except:
            print("erro ao adcionar")
    return render_template('add.html')

#remover tecido cor,tipo,qtd
@app.route('/tecido/remover')
def remove():
    return render_template('index.html')


@app.route('/view')
def view():
    return render_template('view.html')

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

    