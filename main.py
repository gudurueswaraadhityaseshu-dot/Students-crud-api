from fastapi import FastAPI
from app.database import Base, engine
from app.routes.students import router as students_router

# Create the SQLite tables when the application starts.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="EWB Students Database CRUD API",
    description="Student record management API built with FastAPI and SQLite.",
    version="1.0.0",
)

app.include_router(students_router)


@app.get("/", tags=["Health"])
def home():
    return {
        "message": "EWB Students CRUD API is running",
        "docs": "/docs",
    }
