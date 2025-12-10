from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configuração do Banco de Dados (SQLite - Simples e sem senha)
# O arquivo do banco será criado automaticamente como 'todolist.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'chave_secreta_laboratorio_eng_soft'

db = SQLAlchemy(app)

# --- MODELO DE DADOS (Minimização de dados - LGPD) ---
class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    concluida = db.Column(db.Boolean, default=False)

# --- ROTAS (O Caminho do Site) ---

@app.route('/')
def index():
    # Busca todas as tarefas no banco
    tarefas = Tarefa.query.all()
    return render_template('index.html', tarefas=tarefas)

@app.route('/add', methods=['POST'])
def add():
    # Pega o texto e remove espaços em branco antes e depois (.strip())
    titulo = request.form.get('titulo')
    
    # Só entra aqui se o título existir e não for vazio
    if titulo and titulo.strip():
        nova_tarefa = Tarefa(titulo=titulo)
        db.session.add(nova_tarefa)
        db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/update/<int:id>')
def update(id):
    tarefa = Tarefa.query.get_or_404(id)
    tarefa.concluida = not tarefa.concluida
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    tarefa = Tarefa.query.get_or_404(id)
    db.session.delete(tarefa) # LGPD: Exclusão real do dado
    db.session.commit()
    return redirect(url_for('index'))

# Inicialização
if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Cria o banco automaticamente se não existir
    app.run(host='0.0.0.0', port=5000, debug=True)