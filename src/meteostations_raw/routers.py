from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from src.meteostations_raw import crud, schemas
from src import database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/meteostations", response_model=list[schemas.Meteostation])
def read_meteostations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_meteostations(db, skip, limit)

@router.get("/meteostations/{meteostation_id}", response_model=schemas.Meteostation)
def read_meteostation(meteostation_id: int, db: Session = Depends(get_db)):
    db_meteostation = crud.get_meteostation(db, meteostation_id)
    if db_meteostation is None:
        raise HTTPException(status_code=404, detail="Meteostation not found")
    return db_meteostation

@router.post("/meteostations", response_model=schemas.Meteostation)
def create_new_meteostation(meteostation: schemas.MeteostationCreateUpdate, db: Session = Depends(get_db)):
    return crud.create_meteostation(db=db, meteostation=meteostation)

@router.put("/meteostations/{meteostation_id}", response_model=schemas.Meteostation)
def update_existing_meteostation(meteostation_id: int, meteostation: schemas.MeteostationCreateUpdate, db: Session = Depends(get_db)):
    updated_meteostation = crud.update_meteostation(db=db, meteostation_id=meteostation_id, meteostation=meteostation)
    if updated_meteostation is None:
        raise HTTPException(status_code=404, detail="Meteostation not found")
    return updated_meteostation

@router.delete("/meteostations/{meteostation_id}")
def delete_existing_meteostation(meteostation_id: int, db: Session = Depends(get_db)):
    success = crud.delete_meteostation(db=db, meteostation_id=meteostation_id)
    if not success:
        raise HTTPException(status_code=404, detail="Meteostation not found")
    return {"message": "Meteostation deleted successfully"}
