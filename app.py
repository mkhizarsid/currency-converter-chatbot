from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def home():
    data = request.get_json()
    
    params = data['queryResult']['parameters']
    amount = params['unit-currency'][0]['amount']
    from_currency = params['unit-currency'][0]['currency']
    to_currency = params['currency-name'][0]
    
    response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{from_currency}')
    rates = response.json()['rates']
    rate = rates[to_currency]
    converted = amount * rate
    
    result = f"{amount} {from_currency} = {converted:.2f} {to_currency}"
    
    return jsonify({"fulfillmentText": result})

if __name__ == '__main__':
    app.run(debug=True)