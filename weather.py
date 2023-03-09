import requests

def weather():
    try:
        params = {'q': 'Obinitsa', 'units': 'metric', 'lang': 'ru', 'appid': '1912624fd49c501f2986b6ff90fd0b'}
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
        if not response:
            raise
        w = response.json()
        print(w)
        return f"На улице {w['weather'][0]['description']}, {round(w['main']['temp'])} градусов"
    except:
        return 'Не получилось узнать погоду'


list_weather = weather()
print(list_weather)
