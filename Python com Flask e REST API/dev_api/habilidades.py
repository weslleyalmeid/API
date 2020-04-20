from flask_restful import Resource

lista_habilidades = ('Python Java Flask PHP').split()

class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = request.data
        # posicao = len(desenvolvedores)
        # dados['id'] = posicao
        lista_habilidades.append(dados)
        return 'Habilidades adicionada com sucesso!'