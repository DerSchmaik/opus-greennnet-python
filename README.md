## OPUS greenNet python API wrapper
This library provides a simple and convenient way to interact with the OPUS SmartHome Gateway using Python. With this library, you can easily control your OPUS SmartHome devices and build your own custom applications.

Please note that this is my first ever published library for Python, so there may be some rough edges. However, I encourage you to give it a try and provide feedback to help me improve it.


## Supported Devices
### Switch
- [x] [OPUS BRiDGE 1 Channel](https://myopus.eu/en/products/smarthome/switch/1/opus-bridge-1-channel?number=563.010-C)
- [x] [OPUS BRiDGE 2 Channel](https://myopus.eu/en/products/smarthome/switch/7/opus-bridge-2-channel?c=74)
- [x] [OPUS BRiDGE Roller shutter / Venetian blind](https://myopus.eu/en/products/smarthome/switch/8/opus-bridge-roller-shutter/venetian-blind?c=74)
- [x] [OPUS BRIDGE Universaldimmer](https://myopus.eu/en/products/smarthome/switch/352/opus-bridge-universaldimmer?c=74)
- [ ] [OPUS BRiDGE 1 channel, 16A](https://myopus.eu/en/products/smarthome/switch/22/opus-bridge-1-channel-16a?c=74)
- [ ] [OPUS actuator "Professional" round](https://myopus.eu/en/products/smarthome/switch/24/opus-actuator-professional-round?c=74)

### Monetoring
- [ ] OPUS smoke detector 
- [ ] OPUS door/window contact 
- [ ] Any Motion sensor
- [ ] Any Water detector
- [ ] Any Handle sensor
- [ ] Any Temperature / Heat sensor

## Usage

To get started with the OPUS GreenNet Python API Wrapper, you will need to set up an authentication object using the `Auth` class. You can then use this object to create an instance of the `OPUSAPI` class, which you can use to interact with your OPUS SmartHome devices.

Here is an example of how to set up the authentication object and create an instance of the `OPUSAPI` class:

``` Python
# import the libary
import opus_greennet

# create the Auth object to authenticate with the API
# the password can be found on a sticker on your gateway
auth = Auth('http://IP_OF_YOUR_GATEWAY:8080', 'PASSWORD_OF_YOUR_GATEWAY')

# create the OPUS object and pass the auth
opus = OPUSAPI(auth)
```

Once you have set up the authentication object and created an instance of the `OPUSAPI` class, you can start interacting with your OPUS SmartHome devices.

Here is an example of how to print all switches to the console:

``` Python
# get all onechannel switches
# other types: two_channel_switches, blind_switches, dimming_switches
one_channel_switches = opus.get_one_channel_switches()

# print information for every switch
for switch in one_channel_switches:
  # available propertys: name, id, state, location, manufacturer, productId 
  # for two channel switches you have state_1 and state_2 instead of state
  print(f"{switch.name} with ID '{switch.id} is located at {switch.location} with state {switch.state}")
```

Finally, here is an example of how to change the state of a device:

``` Python
# change the state of the first switch in list using change_state
one_channel_switches[0].change_state(True)

# for two channel switches you have to use change_state_1 and change_state_2 instead of change_state
# for dimmers and blinds the state is represented in integers from 0-100 instead of bools
```


## Some info about the API

The REST API is exposed by the [OPUS SmartHome Gateway](https://myopus.eu/en/products/smarthome/control/10/opus-smarthome-gateway) at port 8080. There you will also find a UI where you can test and discover the API. To access the API, you will need to authenticate yourself using the following credentials:
- Username: "admin"
- Password: on a sticker on the OPUS SmartHome Gateway. (8 characters long and consists of capital letters and numbers  e.g. "GBA7VD3G")

![Screenshot_20220107_153159](https://user-images.githubusercontent.com/47828495/148558617-0cfde238-e2c6-42c3-acdf-7ef90466e2d7.png)
The UI should look like this
