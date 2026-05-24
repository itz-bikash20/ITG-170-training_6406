from sqlalchemy import Column, String
from app.database import Base

class Role(Base):

    __tablename__ = "roles"

    role_id = Column(String(1), primary_key=True)
    role_name = Column(String(50), nullable=False)