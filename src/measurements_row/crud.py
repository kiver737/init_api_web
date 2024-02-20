# from sqlalchemy.orm import Session
# from src.measurements_row import models, schemas
# from .models import MeasurementRowModel
# from .schemas import MeasurementRowCreateUpdate, MeasurementRow
#
# def get_measurement_rows(db: Session):
#     return db.query(MeasurementRowModel).all()
#
#
#
#
#
# def get_measurement_row(db: Session, sensor: int):
#     return db.query(MeasurementRowModel).filter(MeasurementRowModel.sensor == sensor).first()
#
# def create_measurement_row(db: Session, measurement_row: MeasurementRowCreateUpdate):
#     new_measurement_row = MeasurementRowModel(
#         sensor=measurement_row.sensor,
#         measurement_value=measurement_row.measurement_value,
#         measurements=measurement_row.measurements,
#         measurement_ts=measurement_row.measurement_ts,
#         meteostation_id=measurement_row.meteostation_id
#     )
#     db.add(new_measurement_row)
#     db.commit()
#     db.refresh(new_measurement_row)
#     return new_measurement_row
#
# def update_measurement_row(db: Session, sensor: int, measurement_row: MeasurementRowCreateUpdate):
#     db_measurement_row = get_measurement_row(db, sensor)
#     if db_measurement_row:
#         db_measurement_row.measurement_value = measurement_row.measurement_value
#         db_measurement_row.measurements = measurement_row.measurements
#         db_measurement_row.measurement_ts = measurement_row.measurement_ts
#         db_measurement_row.meteostation_id = measurement_row.meteostation_id
#         db.commit()
#         return db_measurement_row
#     else:
#         return None
#
# def delete_measurement_row(db: Session, sensor: int):
#     db_measurement_row = get_measurement_row(db, sensor)
#     if db_measurement_row:
#         db.delete(db_measurement_row)
#         db.commit()
#         return True
#     return False
from sqlalchemy import select
from sqlalchemy.orm import Session
from .models import MeasurementRowModel, SensorModel, MeteostationModel, MeasurementTypeModel
from .schemas import MeasurementRowCreateUpdate



# Получение всех записей измерений
# def get_measurement_rows(db: Session):
#
#     return (db.query(
#         MeasurementRowModel.sensor_id,
#         MeasurementRowModel.measurent_value,
#         MeasurementRowModel.measurments,
#         MeasurementRowModel.measurement_ts,
#         MeasurementRowModel.meteostation_id,
#         SensorModel.sensor_name)
#             .join(SensorModel).all())

def get_measurement_rows(db: Session):

    return (db.query(
        MeasurementRowModel.sensor_id,
        MeasurementRowModel.measurent_value,
        MeasurementTypeModel.type_name,
        MeasurementRowModel.measurement_ts,
        MeteostationModel.meteostation_name,
        SensorModel.sensor_name)
        .join(SensorModel)
        .join(MeteostationModel)
        .join(MeasurementTypeModel)
        .all())







# Получение одной записи измерений по ID
def get_measurement_row(db: Session, row_id: int):
    return db.query(MeasurementRowModel).filter(MeasurementRowModel.id == row_id).first()

# Создание новой записи измерений
def create_measurement_row(db: Session, measurement_row: MeasurementRowCreateUpdate):
    new_measurement_row = MeasurementRowModel(
        sensor=measurement_row.sensor,
        measurement_value=measurement_row.measurement_value,
        measurements=measurement_row.measurements,
        measurement_ts=measurement_row.measurement_ts,
        meteostation_id=measurement_row.meteostation_id
    )
    db.add(new_measurement_row)
    db.commit()
    db.refresh(new_measurement_row)
    return new_measurement_row

# Обновление существующей записи измерений
def update_measurement_row(db: Session, row_id: int, measurement_row: MeasurementRowCreateUpdate):
    db_measurement_row = get_measurement_row(db, row_id)
    if db_measurement_row:
        db_measurement_row.sensor = measurement_row.sensor
        db_measurement_row.measurement_value = measurement_row.measurement_value
        db_measurement_row.measurements = measurement_row.measurements
        db_measurement_row.measurement_ts = measurement_row.measurement_ts
        db_measurement_row.meteostation_id = measurement_row.meteostation_id
        db.commit()
        return db_measurement_row
    else:
        return None

# Удаление существующей записи измерений
def delete_measurement_row(db: Session, row_id: int):
    db_measurement_row = get_measurement_row(db, row_id)
    if db_measurement_row:
        db.delete(db_measurement_row)
        db.commit()
        return True
    return False











