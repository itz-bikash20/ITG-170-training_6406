from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from app.security.oauth2 import verify_token

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.employee_model import Employee
from app.models.role_model import Role
from app.models.status_model import EmployeeStatus

from app.schemas.employee_schema import EmployeeCreate

from app.utils.mail_generator import generate_corporate_mail
from app.utils.password_generator import generate_password

router = APIRouter()


# ADD EMPLOYEE
@router.post("/add")
def add_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db),
    hr=Depends(verify_token)
):

    role = db.query(Role).filter(
        Role.role_id == employee.role_id
    ).first()

    if not role:

        raise HTTPException(
            status_code=404,
            detail="Invalid Role ID"
        )

    status = db.query(EmployeeStatus).filter(
        EmployeeStatus.status_id == employee.status_id
    ).first()

    if not status:

        raise HTTPException(
            status_code=404,
            detail="Invalid Status ID"
        )

    existing_employee = db.query(Employee).filter(
        Employee.personal_mail
        == employee.personal_mail
    ).first()

    if existing_employee:

        raise HTTPException(
            status_code=400,
            detail="Employee already exists"
        )

    corporate_mail = generate_corporate_mail(
        employee.fname,
        employee.lname
    )

    password = generate_password(
        employee.fname,
        employee.lname,
        employee.joining_date
    )

    new_employee = Employee(

        fname=employee.fname,

        lname=employee.lname,

        personal_mail=employee.personal_mail,

        corporate_mail=corporate_mail,

        department=employee.department,

        role_id=employee.role_id,

        joining_date=employee.joining_date,

        salary=employee.salary,

        status_id=employee.status_id,

        password=password
    )

    db.add(new_employee)

    db.commit()

    db.refresh(new_employee)

    return {

        "message": "Employee Added Successfully",

        "corporate_mail": corporate_mail,

        "password": password
    }


# FETCH ALL EMPLOYEES
@router.get("/all")
def get_all_employees(
    db: Session = Depends(get_db)
):

    employees = db.query(Employee).all()

    return employees


# FETCH SINGLE EMPLOYEE
@router.get("/{employee_id}")
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    employee = db.query(Employee).filter(
        Employee.employee_id == employee_id
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    return employee
@router.put("/update/{employee_id}")
def update_employee(

    employee_id: int,

    employee: EmployeeCreate,

    db: Session = Depends(get_db),

    hr=Depends(verify_token)
):

    existing_employee = db.query(Employee).filter(
        Employee.employee_id == employee_id
    ).first()

    if not existing_employee:

        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    existing_employee.fname = employee.fname

    existing_employee.lname = employee.lname

    existing_employee.personal_mail = employee.personal_mail

    existing_employee.department = employee.department

    existing_employee.role_id = employee.role_id

    existing_employee.joining_date = employee.joining_date

    existing_employee.salary = employee.salary

    existing_employee.status_id = employee.status_id

    db.commit()

    return {
        "message": "Employee Updated Successfully"
    }
@router.delete("/delete/{employee_id}")
def delete_employee(

    employee_id: int,

    db: Session = Depends(get_db),

    hr=Depends(verify_token)
):

    employee = db.query(Employee).filter(
        Employee.employee_id == employee_id
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    db.delete(employee)

    db.commit()

    return {
        "message": "Employee Deleted Successfully"
    }