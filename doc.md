Após clonar o projeto:
python -m virtualenv .venv

# Windows
.venv\Scripts\activate

Instale as dependências:
pip install -r requirements.txt

Crie o banco de dados:
python manage.py makemigrations
python manage.py migrate

Crie um super usuário:
python manage.py createsuperuser

Execute o servidor:
python manage.py runserver

