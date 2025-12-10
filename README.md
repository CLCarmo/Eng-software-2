# Eng-software-2

````markdown
# 📋 Gestão de Tarefas (To-Do List)

Aplicação web simples para gestão de tarefas, desenvolvida com foco em qualidade de código e acessibilidade.

## 🛠 Tecnologias Usadas

* **Python & Flask** (Backend robusto e leve)
* **SQLite** (Banco de dados simples e eficiente)
* **HTML/CSS** (Frontend limpo e acessível - normas WCAG)
* **Pytest** (Testes automatizados para garantir a lógica)

---

## Como Rodar o Projeto

Siga este guia rápido para configurar e executar a aplicação em sua máquina local.

### 1. Prepare o Ambiente

Abra o terminal na pasta do projeto e execute os comandos abaixo:

```bash
# 1. Crie o ambiente virtual (Recomendado para isolar dependências)
python -m venv venv

# 2. Ative o ambiente virtual

# No Windows (PowerShell):
.\venv\Scripts\activate

# No Linux/Mac/Git Bash:
source venv/bin/activate

# 3. Instale as dependências necessárias
pip install Flask Flask-SQLAlchemy pytest
````

### 2\. Execute a Aplicação

Com o ambiente virtual ativado (`(venv)` deve aparecer no terminal), inicie o servidor:

```bash
python app.py
```

  * **Acesse no navegador:** Abra o link que aparecer no terminal (geralmente [http://127.0.0.1:5000](http://127.0.0.1:5000)).
  * **Uso:** Tente adicionar, concluir e excluir tarefas para testar a persistência dos dados no banco SQLite.

-----

## ✅ Testes e Qualidade

Para verificar se tudo está funcionando conforme as normas (segurança e lógica), rodamos os testes automatizados. Com o terminal aberto e o ambiente ativado, digite:

```bash
pytest
```

Se tudo estiver correto, você verá uma mensagem verde indicando que os testes passaram.

````
