from flask import Flask, make_response, jsonify, request
from bd import carros

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def root():
    return "<h1>API de Carros</h1>" 

@app.route('/carros', methods=['GET'])
def get_carros():
    return make_response(jsonify(
        mensagem='Lista de Carros',
        carros=carros))

@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json
    carros.append(carro)
    return make_response(jsonify(
        mensagem='Carro cadastrado com sucesso.',
        carro=carro     
    ))

@app.route('/carros/<int:carro_id>', methods=['GET'])
def get_carro(carro_id: int):
    carro = carros[carro_id-1]
    if carro:
        return make_response(jsonify(carro=carro))

@app.route('/carros/<int:carro_id>', methods=['DELETE'])
def delete_carros(carro_id: int):
    carro = carros[carro_id-1]
    if carro:
        carros.remove(carro)
    return get_carros()

@app.route('/carros/<int:carro_id>', methods=['PUT'])
def update(carro_id: int):
    body = request.json
    marca = body['marca']
    modelo = body['modelo']
    ano = body['ano']

    carros[carro_id-1]['marca'] = marca
    carros[carro_id-1]['modelo'] = modelo
    carros[carro_id-1]['ano'] = ano
    
    return make_response(jsonify(
        carros=carros[carro_id-1]))
        
app.run(debug=True)