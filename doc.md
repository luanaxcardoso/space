1. Criar um ambiente virtual para o projeto.
### virtualenv venv

2. Ativar o ambiente virtual.
### .\venv\Scripts\Activate.ps1


3. Mostrar todas as dependências do projeto.
### pip freeze

4. Em cada instalação de dependência, adicionar no arquivo requirements.txt. com o comando:
### pip freeze > requirements.txt

5. Instalar o Django.
### pip install django

6. Para ver os comandos do Django.
### django-admin help 

7. Criar um projeto.
### django-admin startproject setup . (O ponto é para não criar mais uma pasta)
    setup é o nome do projeto, pode ser qualquer nome, mas setup ou config é uma boa prática.

*** Dicas  ***
Selecionar - Python interpreter. (venv: venv)
Em settings.py, mudar o TIME_ZONE para America/Sao_Paulo e LANGUAGE_CODE para pt-br.

8. Dotenv é uma biblioteca que permite carregar variáveis de ambiente de um arquivo .env para o seu projeto Python.
### pip install python-dotenv

Criar .env na raiz do projeto.
e adicionar SECRET_KEY=ch retirado do settings.py

### Em settings.py, adicionar:

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = str(os.getenv("SECRET_KEY"))

//////////////////////////////////////////////////////////////////////////////////////////////////////////
Rodar o projeto.
### python manage.py runserver