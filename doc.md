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

7. Criar projeto.
### django-admin startproject setup . (O ponto é para não criar mais uma pasta)
    setup é o nome do projeto, pode ser qualquer nome, mas setup ou config é uma boa prática.

8. Criar app.
### python manage.py startapp galeria

9. Adicionar a app no settings.py.

10. Views e URLs.

11. Em settings adicionar:
STATIC_URL = "static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "setup/static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "static")

12. criar pasta templates na raiz do projeto.

13. criar pasta static em setup

14. rodar o comando collectstatic para juntar todos os arquivos estáticos.
### python manage.py collectstatic

//////////////////////////////////////////////////////////////////////////////////////////////////////////
Em settings.py, mudar o TIME_ZONE para America/Sao_Paulo e LANGUAGE_CODE para pt-br.

Dotenv é uma biblioteca que permite carregar variáveis de ambiente de um arquivo .env para o seu projeto Python.
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