from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open('data.json', 'r') as f:
    data = json.load(f)

# --------------------------------------------------------------------------
@app.route('/cidades', methods=['GET'])
def list_cities():
    city = list({trip['city'] for trip in data['transport']})
    return jsonify({'cidades': city}), 200

def convert_price_to_float(price_str):
    """Converte o preço de string para float."""
    return float(price_str.replace('R$', '').replace(',', '.'))

# --------------------------------------------------------------------------
@app.route('/viagens/<city>', methods=['GET'])
def find_trips(city):
    trips = [trip for trip in data['transport'] if trip['city'].lower() == city.lower()]
    
    most_expensive_trip = max(trips, key=lambda x: convert_price_to_float(x['price_confort']))
    cheapest_trip = min(trips, key=lambda x: convert_price_to_float(x['price_econ']))

    return jsonify({
        'viagem_mais_cara': most_expensive_trip,
        'viagem_mais_barata': cheapest_trip
    }), 200
    
# --------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(port=3000)