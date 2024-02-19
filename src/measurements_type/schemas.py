from pydantic import BaseModel

class MeasurementTypeBase(BaseModel):
    type_id: int
    type_name: str

class MeasurementTypeCreateUpdate(MeasurementTypeBase):
    pass

class MeasurementType(MeasurementTypeBase):
    pass