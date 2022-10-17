import requests
import json
from modules import constants


def read_abi_from_address(address):
    config = constants.CONFIG
    a = address.lower()
    k = config.get("API_KEY")
    base_url = config.get("BASE_URL")
    url = f'{base_url}/api'
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} 

    params = (
        ('module', 'contract'),
        ('action', 'getabi'),
        ('address', address),
        ('apikey', k),
    )    
    json_response = requests.get(url,params=params, headers=headers)
    print(json_response.url)
    if json_response.status_code == 200:
        try:
            json_response = json_response.json()
            return json.loads(json_response['result'])
        except Exception as e:
            print(e)
    else:
        print(json_response)
        return {}
