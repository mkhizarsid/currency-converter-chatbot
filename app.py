from flask import Flask,request,jsonify
import requests

app = Flask(__name__)



@app.route('/webhook',methods=['POST'])
def home():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency'][0]['currency']
    amount = data['queryResult']['parameters']['unit-currency'][0]['amount']
    destination_currency = data['queryResult']['parameters']['currency-name'][0]
    
    response = requests.get('https://api.exchangerate-api.com/v4/latest/'+ source_currency)
    data_api = response.json()
    rates = data_api['rates'][destination_currency]
    converted_amount = amount * rates
    
    
    print(f"Source Currency: {source_currency}, Amount: {amount}, Destination Currency: {destination_currency} , Converted Amount: {converted_amount}")
    return jsonify({"fulfillmentText": "Hello from Flask!"})

if __name__ == '__main__':
    app.run(debug=True)
    
