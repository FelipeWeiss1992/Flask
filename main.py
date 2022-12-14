from flask import Flask, render_template, request, redirect, session, flash, url_for
from model.pessoa import Pessoa
from model.usuario import Usuario

pessoa1 = Pessoa('Felipe', '30', 1.81)
pessoa2 = Pessoa('Haiko', '17', 1.75)
pessoa3 = Pessoa('Jean', '40', 1.85)

lista = [pessoa1,pessoa2,pessoa3]

usuario1 = Usuario('andre', 'andre_vitor', 'moredevs')
usuario2 = Usuario('felipe', 'felipe_weiss', '123')
usuario3 = Usuario('larissa', 'larissa_sebold', '98765')

usuarios = {

    usuario1.nickname: usuario1,
    usuario2.nickname: usuario2,
    usuario3.nickname: usuario3
}

app = Flask(__name__)
app.secret_key = 'moredevs'

@app.route('/')
def login():
    proximo = request.args.get('proximo')
    return render_template('login.html', titulo = 'Login Usuario', proximo = proximo)

@app.route('/listar')
def inicio():
    return render_template('index.html', titulo = 'Lista Pessoas', pessoas = lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proximo = url_for('novo')))

    return render_template('novo.html', titulo = 'Cadastro Pessoa')

@app.route('/criar', methods=['post'])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']

    pessoa = Pessoa(nome, idade, altura)

    lista.append(pessoa)

    return redirect(url_for('inicio'))

@app.route('/autenticar', methods = ['post'])
def autenticar():

    if request.form['usuario'] in usuarios:

        usuario = usuarios[request.form['usuario']]

        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname

            flash(usuario.nickname + ' ' + 'Logado')
            proxima_pagina = request.form['proximo']
        
            return redirect(proxima_pagina)

    else:

        flash('Usuario ou Senha inválidos')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] == None
    flash('Você foi desconectado')
    return redirect(url_for('login'))

app.run(debug=True)