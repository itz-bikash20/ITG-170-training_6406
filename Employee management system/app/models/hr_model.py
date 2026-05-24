from sqlalchemy import Column, Integer, String
from app.database import Base

class HR(Base):

    __tablename__ = "hr_table"

    hr_id = Column(Integer, primary_key=True, index=True)

    hr_name = Column(String(50))

    hr_email = Column(String(100), unique=True)

    hr_password = Column(String(100))