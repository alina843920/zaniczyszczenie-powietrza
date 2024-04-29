import requests

class AirQualityClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_data(self, city):
        url = f"{self.base_url}/city?city={city}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Nie udało się pobrać danych")
BASE_URL = "https://api-docs.iqair.com"  
def get_air_quality(city):
    endpoint = f"{BASE_URL}/city?city={city}"
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("ERROR")