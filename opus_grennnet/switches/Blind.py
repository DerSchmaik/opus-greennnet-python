from ..auth import Auth
from ..helpers import proper_round
import json


class Blind:
  """Class that represents a Blind switch object in the Opus Greennet API."""

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
  def state(self) -> int:
    return int(proper_round(next(value for value in self.raw_data["states"] if value["key"] == "position")["value"]))

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
    """Update the data of the Blind object."""
    self.raw_data = self.auth.get_device(self.id).json()["device"]

  def change_state(self, state: int):
    """Change the state of the OneChannel object."""
    self.auth.putRequest(f'/devices/{self.id}/state', data=json.dumps({'state': {'functions': [{'key': 'position', 'value': state if state <= 100 and state >= 0 else self.state}]}}))
    self.update_data()