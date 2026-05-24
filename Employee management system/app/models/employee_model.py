from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from app.database import Base

class Employee(Base):

    __tablename__ = "employees"

    employee_id = Column(Integer, primary_key=True, index=True)

    fname = Column(String(50))

    lname = Column(String(50))

    personal_mail = Column(String(100), unique=True)

    corporate_mail = Column(String(100), unique=True)

    department = Column(String(50))

    role_id = Column(
        String(1),
        ForeignKey("roles.role_id")
    )

    joining_date = Column(DateTime)

    salary = Column(Float)

    status_id = Column(
        String(1),
        ForeignKey("employee_status.status_id")
    )

    password = Column(String(100))