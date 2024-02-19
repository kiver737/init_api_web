from sqlalchemy import Column, Integer, String
from src.database import Base

class MeasurementTypeModel(Base):
    __tablename__ = 'measurements_type'
    type_id = Column(Integer, primary_key=True)
    type_name = Column(String(256))