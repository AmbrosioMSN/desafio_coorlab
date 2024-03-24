from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open('data.json', 'r') as f:
    data = json.load(f)

# --------------------------------------------------------------------------
@app.route('/cidades', methods=['GET'])
def listar_cidades():
    cidades = list({viagem['city'] for viagem in data['transport']})
    return jsonify({'cidades': cidades}), 200

def convert_price_to_float(price_str):
    """Converte o preço de string para float."""
    return float(price_str.replace('R$', '').replace(',', '.'))

# --------------------------------------------------------------------------
@app.route('/viagens/<cidade>', methods=['GET'])
def buscar_viagens(cidade):
    viagens = [viagem for viagem in data['transport'] if viagem['city'].lower() == cidade.lower()]
    if len(viagens) == 0:
        return jsonify({'message': 'Nenhuma viagem encontrada para a cidade especificada'}), 404
    
    viagem_mais_cara = max(viagens, key=lambda x: convert_price_to_float(x['price_confort']))
    viagem_mais_barata = min(viagens, key=lambda x: convert_price_to_float(x['price_econ']))

    return jsonify({
        'viagem_mais_cara': viagem_mais_cara,
        'viagem_mais_barata': viagem_mais_barata
    }), 200
    
# --------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(port=3000)