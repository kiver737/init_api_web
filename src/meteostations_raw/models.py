from sqlalchemy import Column, Integer, String, Numeric
from src.database import Base

class MeteostationModel(Base):
    __tablename__ = 'meteostations_raw'

    meteostation_id = Column(Integer, primary_key=True)
    meteostation_name = Column(String)
    meteostation_lat = Column(Numeric)
    metistation_long = Column(Numeric)
    metiostation_higth = Column(Integer)
    meteostation_country = Column(String)



