from pydantic import BaseModel

class SensorBase(BaseModel):
    sensor_1d: int
    sensor_name: str

class SensorCreateUpdate(SensorBase):
    pass

class Sensor(SensorBase):
    pass
