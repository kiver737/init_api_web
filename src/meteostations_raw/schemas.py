from pydantic import BaseModel

class MeteostationBase(BaseModel):
    meteostation_id: int
    meteostation_name: str
    meteostation_lat: float
    metistation_long: float
    metiostation_higth: int
    meteostation_country: str

class MeteostationCreateUpdate(MeteostationBase):
    pass

class Meteostation(MeteostationBase):
    pass
