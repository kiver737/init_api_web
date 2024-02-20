from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from src.measurements_row import database, crud, schemas

router = APIRouter()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/measurementrows", response_model=list[schemas.MeasurementRow])
def read_measurement_rows(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_measurement_rows(db)


@router.get("/measurementrows/{sensor_id}", response_model=list[schemas.MeasurementRow])
def read_measurement_row(sensor_id: int, db: Session = Depends(get_db)):
    db_measurement_row = crud.get_measurement_row(db, sensor_id)
    if db_measurement_row is None:
        raise HTTPException(status_code=404, detail="Measurement row not found")
    return db_measurement_row


@router.post("/measurementrows", response_model=schemas.MeasurementRow)
def create_new_measurement_row(measurement_row: schemas.MeasurementRowCreateUpdate, db: Session = Depends(get_db)):
    return crud.create_measurement_row(db=db, measurement_row=measurement_row)


@router.put("/measurementrows/{sensor}", response_model=schemas.MeasurementRow)
def update_existing_measurement_row(sensor: int, measurement_row: schemas.MeasurementRowCreateUpdate,
                                    db: Session = Depends(get_db)):
    updated_measurement_row = crud.update_measurement_row(db=db, sensor=sensor, measurement_row=measurement_row)
    if updated_measurement_row is None:
        raise HTTPException(status_code=404, detail="Measurement row not found")
    return updated_measurement_row


@router.delete("/measurementrows/{sensor}")
def delete_existing_measurement_row(sensor: int, db: Session = Depends(get_db)):
    success = crud.delete_measurement_row(db=db, sensor=sensor)
    if not success:
        raise HTTPException(status_code=404, detail="Measurement row not found")
    return {"message": "Measurement row deleted successfully"}
