from typing import List
from opus_grennnet import OPUSAPI, Auth, OneChannel

def main():
    auth = Auth('http://192.168.178.88:8080', '0582D3EB')
    opus = OPUSAPI(auth)

    lights = opus.get_one_channel_switches()
    
    for light in lights: print(f"{light.name} with ID {light.id} is located at {light.location} with state {light.state}")

main()