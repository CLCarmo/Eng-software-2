import pytest
from app import app, db, Tarefa

@pytest.fixture(scope='module')
def client():
    # Configura para usar banco em MEMÓRIA (não afeta seu arquivo real)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' 
    
    # Cria o cliente de teste
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # GARANTIA: Limpa qualquer lixo anterior
            db.session.query(Tarefa).delete()
            db.session.commit()
            
        yield client
        # Limpeza pós-teste (opcional)

def test_index_carregamento(client):
    response = client.get('/')
    assert response.status_code == 200

def test_adicionar_tarefa(client):
    with app.app_context():
        # Limpa antes de começar para garantir contagem zero
        db.session.query(Tarefa).delete()
        db.session.commit()
        
    response = client.post('/add', data={'titulo': 'Tarefa Teste'}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Tarefa Teste" in response.data

def test_adicionar_vazio_nao_cria(client):
    # Tenta criar vazia
    client.post('/add', data={'titulo': ''}, follow_redirects=True)
    
    with app.app_context():
        # Deve ter APENAS a 'Tarefa Teste' criada no teste anterior
        assert Tarefa.query.count() == 1