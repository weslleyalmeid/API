Curso de Flask do youtube.
https://www.youtube.com/watch?v=r40pC9kyoj0&list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX

instalar virtual env
pip install virtualenv

criar virtual eve
virtualenv [opções] <nome_da_pasta>

ativar
cd nomepasta/script/active

instalar flask no venv
pip install flask

após instalado criar um requeriments
pip freeze > requeriments.txt

para instalar requerimentos 
pip install -r requeriments.txt

execução
python run.py runserver

para atualizar o banco de dados
python run.py db migrate
python run.py db upgrade
