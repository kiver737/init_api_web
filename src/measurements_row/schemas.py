from pydantic import BaseModel
from datetime import datetime

# class MeasurementRowBase(BaseModel):
#     sensor_id: int
#     measurent_value: str
#     measurments: int
#     measurement_ts: datetime
#     meteostation_id: int
#     sensor_name: str

class MeasurementRowBase(BaseModel):
    sensor_id: int
    measurent_value: str
    type_name: str  # instead of measurments
    measurement_ts: datetime
    meteostation_name: str  # instead of meteostation_id
    sensor_name: str




class MeasurementRowCreateUpdate(MeasurementRowBase):
    pass

class MeasurementRow(MeasurementRowBase):
    pass
