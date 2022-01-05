from typing import List
from .auth import Auth
from .switches import Blind, Dimmer, OneChannel, TwoChannel

class OPUSAPI:
    """Class to communicate with the OPUS API"""
    
    def __init__(self, auth: Auth) -> None:
        """Initialize the API and store the auth so we can make requests."""
        self.auth = auth
        
    def get_one_channel_switches(self) -> List[OneChannel]:
        r = self.auth.getOneChannelSwitches()
        return [OneChannel(device, self.auth) for device in r]

    def get_two_channel_switches(self) -> List[TwoChannel]:
        r = self.auth.getTwoChannelSwitches()
        return [TwoChannel(device, self.auth) for device in r]
    
    def get_blind_switches(self) -> List[Blind]:
        r = self.auth.getBlindSwitches()
        return [Blind(device, self.auth) for device in r]
    
    def get_dimming_switches(self) -> List[Dimmer]:
        r = self.auth.getDimmerSwitches()
        return [Dimmer(device, self.auth) for device in r]
    
    @property
    def serialNumber(self) -> str:
        r = self.auth.request('GET', '/system/info').json()
        return r["systemInfo"]["serialNumber"]
        
        