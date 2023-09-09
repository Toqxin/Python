import requests
import time

while True:

    city = input("Enter city name:")

    if city != 'stop':
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YourApiKey'

        responce = requests.get(url)
        if responce.status_code == 200:
            data = responce.json()

            city = data['name']
            statement = data['weather'][0]['description']
            temperature = data['main']['temp']
            celcius = temperature-273.15
            humidity = data['main']['humidity']

            print(f'{city} city weather: {statement}')
            print(f'Temperature: {celcius}°C')
            print(f'Humidity: {humidity}%')
        else:
            print('Weather information not found...')
        print("-----------------<>-----------------")
    else:
        print("Exiting...")
        time.sleep(3)
        break
