from app.run import app
from flask import Flask,render_template,url_for,request,redirect,jsonify
from flask_sqlalchemy import SQLAlchemy



#adcionar tecido cor ,tipo, qtd
@app.route('/tecido/add')
def index():
    return render_template('index.html')

#remover tecido cor,tipo,qtd
@app.route('/tecido/remover')
def index():
    return render_template('index.html')


@app.route('/view')
def index():
    return render_template('index.html')