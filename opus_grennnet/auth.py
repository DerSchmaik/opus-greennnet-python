import requests
from requests.api import request

class Auth:
    """Class to make authenticated requests to the OPUS Greennet API"""

    def __init__(self, host: str, password: str, **kwargs):
        """Initialize the Auth class"""
        self.host = host
        self.username = kwargs.get('username', 'admin')
        self.password = password
        self.status()
        
    @property
    def status(self) -> bool:
        r = self.request("GET", "/system/info")
        if r: return True
        else: 
            raise ConnectionError("Invalid host or password")
        

    def request(self, method: str, path: str, **kwargs) -> requests.Response:
        """Make an authenticated request to the OPUS Greennet API"""
        try:
            return requests.request(method, f'{self.host}{path}', auth=(self.username, self.password), headers={'Content-type': 'application/json'}, **kwargs)
        except:
            return None
    
    def putRequest(self, path: str, **kwargs) -> requests.Response:
        """Make an authenticated PUT request to the OPUS Greennet API"""
        return requests.put(f'{self.host}{path}', auth=(self.username, self.password), headers={'Content-type': 'application/json'}, **kwargs)
    
    
    def get_device(self, device_id: str) -> dict:
        """Get the data of a device"""
        return self.request('GET', f'/devices/{device_id}')

    def getAll(self):
        return self.request('GET', '/devices').json()['devices']

    def getBlindSwitches(self):
        r = self.request('GET', '/devices/')
        return [device for device in r.json()['devices'] if device['productId'] == "004000000004"]

    def getOneChannelSwitches(self):
        r = self.request('GET', '/devices')
        return [device for device in r.json()['devices'] if device['productId'] == "004000000005"]

    def getTwoChannelSwitches(self):
        r = self.request('GET', '/devices')
        return [device for device in r.json()['devices'] if device['productId'] == "004000000006"]

    def getDimmerSwitches(self):
        r = self.request('GET', '/devices')
        return [device for device in r.json()['devices'] if device['productId'] == "00400000001B" or device["productId"] == "004000000003"]

    def getSmokeDetectors(self):
        r = self.request('GET', '/devices')
        return [device for device in r.json()['devices'] if device['productId'] == "00401000002E"]
