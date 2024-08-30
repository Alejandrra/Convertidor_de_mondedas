from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

# Tu API key obtenida de ExchangeRate-API
api_key = "cc9c058e4835cbdb16501129"
base_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

@app.route('/')
def index():
    return render_template('index.html')  # Asegúrate de que index.html está en la carpeta 'templates'

@app.route('/convert', methods=['GET'])
def convert_currency():
    base_currency = request.args.get('base')
    target_currency = request.args.get('target')
    amount = float(request.args.get('amount'))

    # Hacer la solicitud a la API
    response = requests.get(f"{base_url}{base_currency}")
    data = response.json()

    # Obtener la tasa de cambio
    exchange_rate = data['conversion_rates'][target_currency]
    converted_amount = amount * exchange_rate

    return jsonify({
        'base_currency': base_currency,
        'target_currency': target_currency,
        'amount': amount,
        'converted_amount': converted_amount
    })

if __name__ == '__main__':
    app.run(debug=True)
