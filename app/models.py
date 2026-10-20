from sqlalchemy import Column, Date, Integer, String
from app.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False, index=True)
    date_of_birth = Column(Date, nullable=False)
    email = Column(String(254), unique=True, index=True, nullable=True)
    phone = Column(String(30), nullable=True)
    course = Column(String(120), nullable=True)
    address = Column(String(250), nullable=True)
