# Django-contas-controle-gastos
Projeto Python Django para administrar os dados das contas e controle de gastos de uma empresa

Sistema criado com Django, para controle de contas e de gastos

Digitar os comandos no seu terminal:    

    1 - Criar uma venv:
        python3 -m venv venv

    2 - Ativar a venv:
        venv/bin/activate (Linux e Mac)
        Scriptsactivate (Windows)

    3 - Instalar o Django:
        pip install django

    4 - Criar esse projeto, após a instalação completa do Django:
        django-admin startproject controle_gastos .
    
    5 - Criar a aplicação desse projeto:
        python manage.py startapp contas

    6 - Fazer o migrate do banco de dados:
        python manage.py migrate

    7 - Rodar o sistema em sua máquina local:
        python manage.py runserver