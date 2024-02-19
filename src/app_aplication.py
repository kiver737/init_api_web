from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src.sensors import schemas, database, models, crud
from src.sensors import routers
from src.measurements_type import routers as measurements
from src.meteostations_raw import routers as metio
from src.measurements_row import routers as measurements_row

app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)

app.include_router(routers.router)
app.include_router(measurements.router)
app.include_router(metio.router)
app.include_router(measurements_row.router)

# Запуск сервера FastAPI (при необходимости)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
