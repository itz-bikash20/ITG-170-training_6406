from sqlalchemy import Column, String
from app.database import Base

class EmployeeStatus(Base):

    __tablename__ = "employee_status"

    status_id = Column(String(1), primary_key=True)

    status_name = Column(String(50), nullable=False)