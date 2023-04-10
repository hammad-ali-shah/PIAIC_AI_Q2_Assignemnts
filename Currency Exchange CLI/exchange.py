import requests
import json

api_key = 'VW2sgZ6I5fKcGlctLzrkVDLaM0P399ll'
url = f'https://api.exchangeratesapi.io/latest?access_key={api_key}'

# Get user inputs
source_currency = input('Enter source currency: ')
target_currency = input('Enter target currency: ')
amount = float(input('Enter amount to be converted: '))

# Send request to API
params = {'base': source_currency, 'symbols': target_currency}
headers = {'Accept': 'application/json'}
response = requests.get(url, params=params, headers=headers)

# Parse API response
if response.status_code == 200:
    data = json.loads(response.text)
    if 'rates' in data and target_currency in data['rates']:
        exchange_rate = data['rates'][target_currency]

        # Calculate converted amount
        converted_amount = amount * exchange_rate

        # Display converted amount
        print(f'{amount} {source_currency} = {converted_amount:.2f} {target_currency}')
    else:
        print(f'Error: Exchange rate for {target_currency} not found')
else:
    print('Error fetching exchange rates')
