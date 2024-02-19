from sqlalchemy.orm import Session
from src.measurements_type import models, schemas




def get_measurement_types(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.MeasurementTypeModel).offset(skip).limit(limit).all()

def get_measurement_type(db: Session, type_id: int):
    return db.query(models.MeasurementTypeModel).filter(models.MeasurementTypeModel.type_id == type_id).first()

def create_measurement_type(db: Session, measurement_type: schemas.MeasurementTypeCreateUpdate):
    db_measurement_type = models.MeasurementTypeModel(type_id=measurement_type.type_id, type_name=measurement_type.type_name)
    db.add(db_measurement_type)
    db.commit()
    db.refresh(db_measurement_type)
    return db_measurement_type

def update_measurement_type(db: Session, type_id: int, measurement_type: schemas.MeasurementTypeCreateUpdate):
    db_measurement_type = get_measurement_type(db, type_id)
    if db_measurement_type:
        db_measurement_type.type_name = measurement_type.type_name
        db.commit()
        return db_measurement_type
    else:
        return None

def delete_measurement_type(db: Session, type_id: int):
    db_measurement_type = get_measurement_type(db, type_id)
    if db_measurement_type:
        db.delete(db_measurement_type)
        db.commit()
        return True
    return False
