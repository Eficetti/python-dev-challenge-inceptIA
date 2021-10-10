import requests, json
class GeoAPI:
    API_KEY = "d610f567c28f1d2151a05a8681367d8d"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"

    @classmethod
    def is_hot_in_pehuajo(cls):    
        r = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=-35.836948753554054&lon=-61.870523905384076&appid=d610f567c28f1d2151a05a8681367d8d&units=metric")
        data = json.loads(r.text)
        temperature = data['current']['temp']
        if temperature > 28 and response.status_code == 200:
            return True
        else:
            return False
        

c = GeoAPI
c.is_hot_in_pehuajo()