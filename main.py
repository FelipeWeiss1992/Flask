from flask import Flask, render_template, request, redirect, session, flash
from pessoa import Pessoa

pessoa1 = Pessoa('Felipe', '30', 1.81)
pessoa2 = Pessoa('Haiko', '17', 1.75)
pessoa3 = Pessoa('Jean', '40', 1.85)


lista = [pessoa1,pessoa2,pessoa3]

app = Flask(__name__)
app.secret_key = 'moredevs'

@app.route('/')
def login():
    return render_template('login.html', titulo = 'Login Usuario')

@app.route('/listar')
def inicio():
    return render_template('index.html', titulo = 'Lista Pessoas', pessoas = lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/')

    return render_template('novo.html', titulo = 'Cadastro Pessoa')

@app.route('/criar', methods=['post'])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']

    pessoa = Pessoa(nome, idade, altura)

    lista.append(pessoa)

    return redirect('/listar')

@app.route('/autenticar', methods = ['post'])
def autenticar():
    if 'moredevs' == request.form['senha']:

        session['usuario_logado'] = request.form['usuario']

        flash(session['usuario_logado'] + ' ' + 'Logado')
        return redirect('/listar')

    else:
        flash('Senha incorreta')
        return redirect('/')

@app.route('/logout')
def logout():
    session['usuario_logado'] == None
    flash('Você foi desconectado')
    return redirect('/')

app.run(debug=True)