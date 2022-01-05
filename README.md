# ExperienceIn
Instituto Federal de Educação, Ciência e Tecnologia de Brasília  
Tecnólogo em Sistemas para Internet - Turma TSIV5A  
Programação para Internet 2 - Prof. Fábio Henrique

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&style=plastic&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?logo=django&style=plastic)
### [![ExperienceIn](https://img.shields.io/badge/ExperienceIn-acesse-000?style=social&logo=expensify)](http://tiagocf2.pythonanywhere.com/)  
---

## Sobre
O *ExperienceIn* é um projeto de faculdade da matéria de Programação para Internet 2, no qual os alunos deveriam criar um *webapp* em Python com Django. Esse *webapp* se trata basicamente de um sistema de cadastro e login de perfis, também com um sistema de amigos.

## Instalação
Para rodar o projeto em sua máquina, primeiramente [baixe os arquivos](https://github.com/Tiagocf2/ppi2/archive/refs/heads/main.zip) do projeto.  
Ou clone o repositório para sua máquina 
```shell
$ git clone https://github.com/Tiagocf2/experiencein.git
```

<br>
Navegue para a pasta do projeto, depois faça o comando de migração para criar o banco de dados.

```shell
$ cd experiencein

$ python manage.py migrate
```
Por fim será preciso modificar o arquivo de configurações `experiencein/settings.py` da seguinte maneira:  
<br>
Mude `DEBUG` para `True` e remova tudo de `ALLOWED_HOSTS`.

```python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
```
Depois remova o campo `STATIC_ROOT`.

```python
STATIC_URL = '/static/'

#Remova essa linha
STATIC_ROOT = '/home/tiagocf2/experiencein/static'
```
Por fim inicie o servidor!

```shell
$ python manage.py runserver
```
E acesse pelo link http://localhost:8000.  
<br>

## Link da Aplicação
Também é possível acessar a aplicação hosteada na nuvem.  
**http://tiagocf2.pythonanywhere.com/**






