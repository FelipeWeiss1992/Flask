from flask import render_template, request, redirect, session, flash, url_for
from main import app, db
from models.pessoas import Pessoas
from models.usuarios import Usuarios

@app.route('/')
def login():

    lista = Pessoas.query.order_by(Pessoas.id)

    return render_template('login.html', titulo = 'Login Usuario', pessoas = lista)

@app.route('/autenticar', methods=['POST'])
def autenticar():

    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    if usuario:
        
        if request.form['senha'] == usuario.senha:

            session['usuario_logado'] = usuario.nickname
            

            flash(usuario.nickname + ' ' + 'logado com sucesso')

            proxima_pagina = request.form['proximo']

            return redirect(proxima_pagina)

    else:
        flash('Usuário ou Senha incorretos. Tente novamente')
        #dinamizando url

        return redirect(url_for('login'))

@app.route('/listar')
def inicio():

    lista = Pessoas.query.order_by(Pessoas.id)

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

    pessoa = Pessoas.query.filter_by(nome=nome).first()

    if pessoa:
        flash('Pessoa já existente.')
        return redirect(url_for('inicio'))
    
    nova_pessoa = Pessoas(nome = nome, idade = idade, altura = altura)

    db.session.add(nova_pessoa)

    db.session.commit()

    return redirect(url_for('inicio'))

@app.route('/logout')
def logout():

    session['usuario_logado'] == None

    flash('Você foi desconectado')  

    return redirect(url_for('login'))

@app.route('/editar/<int:id>')
def editar(id):

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proximo = url_for('editar')))
        
    pessoa = Pessoas.query.filter_by(id=id).first()
    return render_template('editar.html', titulo = 'Editar Pessoa', pessoa = pessoa)

@app.route('/atualizar', methods = ['post'])
def atualizar():
    pessoa = Pessoas.query.filter_by(id=request.form['id']).first()
    
    pessoa.nome = request.form['nome']
    pessoa.idade = request.form['idade']
    pessoa.altura = request.form['altura']

    db.session.add(pessoa)
    db.session.commit()
    return redirect(url_for('inicio'))

@app.route('/Deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login'))

    Pessoas.query.filter_by(id=id).delete()
    db.session.commit()
    flash(f'Deletado com sucesso')
    return redirect(url_for('inicio'))

