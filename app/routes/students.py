from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.database import get_db
from app.models import Student
from app.schemas import StudentCreate, StudentRead, StudentUpdate

router = APIRouter(prefix="/students", tags=["Students"])


@router.post("", response_model=StudentRead, status_code=status.HTTP_201_CREATED)
def create_student(payload: StudentCreate, db: Session = Depends(get_db)):
    if payload.email:
        existing = db.query(Student).filter(Student.email == str(payload.email)).first()
        if existing:
            raise HTTPException(status_code=409, detail="A student with this email already exists.")
    student = Student(**payload.model_dump())
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


@router.get("", response_model=list[StudentRead])
def list_students(
    search: str | None = Query(default=None, description="Search name, email, or course"),
    db: Session = Depends(get_db),
):
    query = db.query(Student)
    if search:
        term = f"%{search}%"
        query = query.filter(
            or_(Student.name.ilike(term), Student.email.ilike(term), Student.course.ilike(term))
        )
    return query.order_by(Student.id.asc()).all()


@router.get("/{student_id}", response_model=StudentRead)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
    return student


@router.patch("/{student_id}", response_model=StudentRead)
def update_student(student_id: int, payload: StudentUpdate, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")

    updates = payload.model_dump(exclude_unset=True)
    if "email" in updates and updates["email"]:
        duplicate = db.query(Student).filter(
            Student.email == str(updates["email"]), Student.id != student_id
        ).first()
        if duplicate:
            raise HTTPException(status_code=409, detail="A student with this email already exists.")

    for field, value in updates.items():
        setattr(student, field, value)
    db.commit()
    db.refresh(student)
    return student


@router.put("/{student_id}", response_model=StudentRead)
def replace_student(student_id: int, payload: StudentCreate, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
    if payload.email:
        duplicate = db.query(Student).filter(
            Student.email == str(payload.email), Student.id != student_id
        ).first()
        if duplicate:
            raise HTTPException(status_code=409, detail="A student with this email already exists.")
    for field, value in payload.model_dump().items():
        setattr(student, field, value)
    db.commit()
    db.refresh(student)
    return student


@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
    db.delete(student)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
