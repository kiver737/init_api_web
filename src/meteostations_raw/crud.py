from sqlalchemy.orm import Session
from src.meteostations_raw import models, schemas

def get_meteostations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.MeteostationModel).offset(skip).limit(limit).all()

def get_meteostation(db: Session, meteostation_id: int):
    return db.query(models.MeteostationModel).filter(models.MeteostationModel.meteostation_id == meteostation_id).first()

def create_meteostation(db: Session, meteostation: schemas.MeteostationCreateUpdate):
    db_meteostation = models.MeteostationModel(
        meteostation_id=meteostation.meteostation_id,
        meteostation_name=meteostation.meteostation_name,
        meteostation_lat=meteostation.meteostation_lat,
        metistation_long=meteostation.metistation_long,
        metiostation_higth=meteostation.metiostation_higth,
        meteostation_country=meteostation.meteostation_country
    )
    db.add(db_meteostation)
    db.commit()
    db.refresh(db_meteostation)
    return db_meteostation

def update_meteostation(db: Session, meteostation_id: int, meteostation: schemas.MeteostationCreateUpdate):
    db_meteostation = get_meteostation(db, meteostation_id)
    if db_meteostation:
        db_meteostation.meteostation_name = meteostation.meteostation_name
        db_meteostation.meteostation_lat = meteostation.meteostation_lat
        db_meteostation.metistation_long = meteostation.metistation_long
        db_meteostation.metiostation_higth = meteostation.metiostation_higth
        db_meteostation.meteostation_country = meteostation.meteostation_country
        db.commit()
        return db_meteostation
    else:
        return None

def delete_meteostation(db: Session, meteostation_id: int):
    db_meteostation = get_meteostation(db, meteostation_id)
    if db_meteostation:
        db.delete(db_meteostation)
        db.commit()
        return True
    return False
