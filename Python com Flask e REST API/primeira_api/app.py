from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# após a barra do caminho, digitar uma id ou blalboa.com.br/app.ro
@app.route('/<int:id>')
def pessoas(id):
    return jsonify({'id' : id, 'nome' : 'Weslley', 'profissao' : 'Estudante'})

# @app.route('/soma/<int:valor1>/<int:valor2>/<int:valor3>/')
# def soma(valor1, valor2, valor3):
#     return jsonify({'soma' : valor1+valor2+valor3})

@app.route('/soma', methods = ['POST', 'GET'])
def soma():
    if request.method == 'POST': 
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 10 + 10
    return {'soma' : total}

if __name__ == "__main__":
    app.run(debug= True)