import pytest
from app import app, db, Tarefa

# Configura um banco de dados temporário na memória para o teste (não estraga o seu banco real)
@pytest.fixture(scope='module')
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' #

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        # O banco é destruído ao final do teste

# Teste 1: Verifica se a página carrega (Status 200)
def test_index_carregamento(client):
    response = client.get('/')
    assert response.status_code == 200 #

# Teste 2: Verifica se dá para criar uma tarefa
def test_adicionar_tarefa(client):
    response = client.post('/add', data={'titulo': 'Tarefa de Teste Pytest'}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Tarefa de Teste Pytest" in response.data # Confirma se apareceu na página

# Teste 3: Segurança (Não deixar criar tarefa vazia)
def test_adicionar_vazio_nao_cria(client):
    # Tenta enviar sem título
    client.post('/add', data={'titulo': ''}, follow_redirects=True)
    
    with app.app_context():
        # Conta as tarefas: Só deve existir a 'Tarefa de Teste Pytest' do teste anterior
        assert Tarefa.query.count() == 1 #