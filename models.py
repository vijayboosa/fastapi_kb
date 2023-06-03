from pydantic import BaseModel
from typing import Union

class Device(BaseModel):
    deviceName: str
    deviceType: str
    deviceRegion: str
    deviceStatus: str
    deviceOwnerGUID: Union[str, None] = None;

class DeviceLocations(BaseModel):
    latitude: str
    longitude: str
    timestamp: str
    deviceId: Union[str, None] = None;