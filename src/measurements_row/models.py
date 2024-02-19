from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from .database import Base


# models.py




class MeasurementRowModel(Base):
    __tablename__ = 'measurements_row'
    sensor_id = Column(Integer, ForeignKey('sensors.sensor_1d'), primary_key=True)
    meteostation_id = Column(Integer)
    measurments = Column(Integer)
    sensor = relationship("SensorModel", back_populates="measurements")
    measurent_value = Column(String)
    measurement_ts = Column(TIMESTAMP)


class SensorModel(Base):
    __tablename__ = 'sensors'
    sensor_1d = Column(Integer, primary_key=True)
    sensor_name = Column(String)
    measurements = relationship(MeasurementRowModel, back_populates="sensor")

