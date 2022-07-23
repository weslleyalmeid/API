from fastapi import FastAPI
import json

app = FastAPI()


vendas = {
    1: {"item":"lata","preco_unitario":8, "quantidade":5},
    2: {"item":"garraga","preco_unitario":16, "quantidade":5},
    3: {"item":"copo","preco_unitario":4, "quantidade":5},
    4: {"item":"tampa","preco_unitario":2, "quantidade":5},
    5: {"item":"tampinha","preco_unitario":1, "quantidade":5},
}

@app.get('/')
def home():
    # return json.dumps({"Vendas": len(vendas)})
    return {"Vendas": len(vendas)}


@app.get('/vendas/{id_venda}')
def pegar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return {'Erro': 'intervalo não atendido'}