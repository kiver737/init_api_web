from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from src.measurements_type import crud, schemas
from src import database


router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/measurementstype", response_model=list[schemas.MeasurementType])
def read_measurement_types(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_measurement_types(db, skip, limit)

@router.get("/measurementstype/{type_id}", response_model=schemas.MeasurementType)
def read_measurement_type(type_id: int, db: Session = Depends(get_db)):
    db_measurement_type = crud.get_measurement_type(db, type_id)
    if db_measurement_type is None:
        raise HTTPException(status_code=404, detail="Measurement type not found")
    return db_measurement_type

@router.post("/measurementstype", response_model=schemas.MeasurementType)
def create_new_measurement_type(measurement_type: schemas.MeasurementTypeCreateUpdate, db: Session = Depends(get_db)):
    return crud.create_measurement_type(db=db, measurement_type=measurement_type)

@router.put("/measurementstype/{type_id}", response_model=schemas.MeasurementType)
def update_existing_measurement_type(type_id: int, measurement_type: schemas.MeasurementTypeCreateUpdate, db: Session = Depends(get_db)):
    updated_measurement_type = crud.update_measurement_type(db=db, type_id=type_id, measurement_type=measurement_type)
    if updated_measurement_type is None:
        raise HTTPException(status_code=404, detail="Measurement type not found")
    return updated_measurement_type

@router.delete("/measurementstype/{type_id}")
def delete_existing_measurement_type(type_id: int, db: Session = Depends(get_db)):
    success = crud.delete_measurement_type(db=db, type_id=type_id)
    if not success:
        raise HTTPException(status_code=404, detail="Measurement type not found")
    return {"message": "Measurement type deleted successfully"}
