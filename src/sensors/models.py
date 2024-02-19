from typing import List

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, relationship
from .database import Base





class SensorModel(Base):
    __tablename__ = 'sensors'
    sensor_1d = Column(Integer, primary_key=True)
    sensor_name = Column(String)
    measurements = relationship("MeasurementRowModel", back_populates="sensor")
