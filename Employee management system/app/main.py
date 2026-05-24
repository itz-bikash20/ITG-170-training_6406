from fastapi import FastAPI

from app.database import engine
from app.database import Base

from app.models.role_model import Role
from app.models.status_model import EmployeeStatus
from app.models.hr_model import HR
from app.models.employee_model import Employee

from app.routes.hr_routes import router as hr_router
from app.routes.employee_routes import router as employee_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(
    hr_router,
    prefix="/hr",
    tags=["HR APIs"]
)

app.include_router(
    employee_router,
    prefix="/employee",
    tags=["Employee APIs"]
)


@app.get("/")
def home():

    return {
        "message": "Employee Management System Running"
    }