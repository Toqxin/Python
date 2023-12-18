import requests
from tabulate import tabulate

while True:
    #API key control
    api_key = input('Enter your API key: ')
    headers = {
        'py_apiKey': api_key
    }

    response = requests.get('http://localhost:3000/api/cars', headers=headers)
    if response.status_code == 403:
        print('Invalid API key. Please try again.')

    else:
        while True:
            choice = input('allData/onlyCar: ')
            #Show All Data
            if choice == 'allData':
                response = requests.get('http://localhost:3000/api/cars', headers=headers)
                data = response.json()
                print(tabulate(data, headers="keys"))
            
            #Show only cars info
            elif choice == 'onlyCar':
                brand = input('Car Name: ')
                response = requests.get(f'http://localhost:3000/api/cars/{brand}', headers=headers)
                data = response.json()
                print(tabulate(data, headers="keys"))
            else:
                print('Error')










