from ..auth import Auth
import json


class TwoChannel:
  """Class that represents a One chanel switch object in the Opus Greennet API."""

  def __init__(self, raw_data: dict, auth: Auth):
    self.raw_data = raw_data
    self.auth = auth

  @property
  def id(self) -> str:
    return self.raw_data["deviceId"]

  @property
  def name(self) -> str:
    return self.raw_data["friendlyId"]

  @property
  def state1(self) -> bool:
    return next(value for value in self.raw_data["states"] if value["channel"] == 0)["value"] == "on"
  
  @property
  def state2(self) -> bool:
    return next(value for value in self.raw_data["states"] if value["channel"] == 1)["value"] == "on"

  @property
  def location(self) -> str:
    return self.raw_data["location"]

  @property
  def manufacturer(self) -> str:
    return self.raw_data["manufacturer"]

  @property
  def productId(self) -> str:
    return self.raw_data["productId"]

  def update_data(self):
    """Update the data of the TwoChannel object."""
    self.raw_data = self.auth.get_device(self.id).json()["device"]

  def change_state1(self, state: bool):
    """Change the first state of teh TwoChannel object."""
    r = self.auth.putRequest(f'/devices/{self.id}/state', data=json.dumps({'state': {'functions': [{'key': 'switch', 'value': 'on' if state else 'off'}, {'key': 'channel', 'value': 0}]}}))
    self.update_data()
  
  def change_state2(self, state: bool):
    """Change the second state of the TwoChannel object."""
    r = self.auth.putRequest(f'/devices/{self.id}/state', data=json.dumps({'state': {'functions': [{'key': 'switch', 'value': 'on' if state else 'off'}, {'key': 'channel', 'value': 1}]}}))
    self.update_data()