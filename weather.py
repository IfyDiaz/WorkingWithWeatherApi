import requests

API_KEY = "Add_api_key"
BASE_URL = "Add_base_url"

city = input('Enter a city name: ')
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)


if response.status_code == 200:
    data = response.json()

    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)
    body_feel = data['main']['feels_like']
    temperature_min = data['main']['temp_min']
    temperature_max = data['main']['temp_max']
    humidity = data['main']['humidity']

    
    print(f"The temperature in {city} is {temperature} but it feels like {body_feel} ")
    print(f"Temperature range {temperature_min}, {temperature_max}")
    print(f"Humidity is {humidity}")

else:
    print("An error occurred.")