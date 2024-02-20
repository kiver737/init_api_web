from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from .database import Base


# models.py




class MeasurementRowModel(Base):
    __tablename__ = 'measurements_row'
    sensor_id = Column(Integer, ForeignKey('sensors.sensor_1d'), primary_key=True)
    meteostation_id = Column(Integer)
    sensor = relationship("SensorModel", back_populates="measurements")
    measurent_value = Column(String)
    measurement_ts = Column(TIMESTAMP)

    meteostation_id = Column(Integer, ForeignKey('meteostations_raw.meteostation_id'))
    meteostation = relationship("MeteostationModel", back_populates="measurements")
    # Add a relationship for measurement type
    measurments = Column(Integer, ForeignKey('measurements_type.type_id'))
    measurements_type = relationship("MeasurementTypeModel", back_populates="measurements")


class SensorModel(Base):
    __tablename__ = 'sensors'
    sensor_1d = Column(Integer, primary_key=True)
    sensor_name = Column(String)
    measurements = relationship(MeasurementRowModel, back_populates="sensor")


class MeteostationModel(Base):
    __tablename__ = 'meteostations_raw'
    meteostation_id = Column(Integer, primary_key=True)
    meteostation_name = Column(String)
    measurements = relationship("MeasurementRowModel", back_populates="meteostation")


class MeasurementTypeModel(Base):
    __tablename__ = 'measurements_type'
    type_id = Column(Integer, primary_key=True)
    type_name = Column(String)
    measurements = relationship(MeasurementRowModel, back_populates="measurements_type")