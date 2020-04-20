
from models import Pessoas, Usuarios


# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome= 'Almeida', idade= 27)
    print(pessoa)
    pessoa.save()


# Consulta dados na tabela pessoa
def consulta_pessoas():
    pessoas= Pessoas.query.all()
    print(pessoas)
    # pessoa = Pessoas.query.filter_by(nome= 'Almeida').first()
    # print(pessoa.idade)


# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome= 'Almeida').first()
    pessoa.nome = 'Rudineilson'
    pessoa.save()


# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome= 'Rudineilson').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login= login, senha= senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)



if __name__ == "__main__":
    # insere_pessoas()
    # consulta_pessoas()
    # altera_pessoa()
    # exclui_pessoa()
    # consulta_pessoas()
    insere_usuario('weslley', '1234')
    insere_usuario('almeida', '4321')
    consulta_todos_usuarios()