from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from src.sensors import database
from src.sensors import crud, schemas



router = APIRouter()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()






@router.get("/sensors", response_model=list[schemas.Sensor])
def read_sensors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_sensors(db, skip, limit)

@router.get("/sensors/{sensor_1d}", response_model=schemas.Sensor)
def read_sensor(sensor_1d: int, db: Session = Depends(get_db)):
    db_sensor = crud.get_sensor(db, sensor_1d)
    if db_sensor is None:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return db_sensor

@router.post("/sensors/", response_model=schemas.Sensor)
def create_new_sensor(sensor: schemas.SensorCreateUpdate, db: Session = Depends(get_db)):
    return crud.create_sensor(db=db, sensor=sensor)

@router.put("/sensors/{sensor_1d}", response_model=schemas.Sensor)
def update_existing_sensor(sensor_1d: int, sensor: schemas.SensorCreateUpdate, db: Session = Depends(get_db)):
    updated_sensor = crud.update_sensor(db=db, sensor_1d=sensor_1d, sensor=sensor)
    if updated_sensor is None:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return updated_sensor

@router.delete("/sensors/{sensor_1d}")
def delete_existing_sensor(sensor_1d: int, db: Session = Depends(get_db)):
    success = crud.delete_sensor(db=db, sensor_1d=sensor_1d)
    if not success:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return {"message": "Sensor deleted successfully"}



