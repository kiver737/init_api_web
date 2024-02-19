from sqlalchemy.orm import Session
from src.sensors import schemas, models


def get_sensors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.SensorModel).offset(skip).limit(limit).all()

def get_sensor(db: Session, sensor_1d: int):
    return db.query(models.SensorModel).filter(models.SensorModel.sensor_1d == sensor_1d).first()

def create_sensor(db: Session, sensor: schemas.SensorCreateUpdate):
    db_sensor = models.SensorModel(sensor_1d=sensor.sensor_1d, sensor_name=sensor.sensor_name)
    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)
    return db_sensor

def update_sensor(db: Session, sensor_1d: int, sensor: schemas.SensorCreateUpdate):
    db_sensor = get_sensor(db, sensor_1d)
    if db_sensor:
        db_sensor.sensor_name = sensor.sensor_name
        db.commit()
        return db_sensor
    else:
        return None

def delete_sensor(db: Session, sensor_1d: int):
    db_sensor = get_sensor(db, sensor_1d)
    if db_sensor:
        db.delete(db_sensor)
        db.commit()
        return True
    return False
