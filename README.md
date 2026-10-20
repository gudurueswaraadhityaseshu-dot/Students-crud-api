# EWB Students Database CRUD API

An individual Python backend project using **FastAPI** and **SQLite**, prepared against the EWB internship assignment. It supports Create, Read, Update and Delete (CRUD) operations for student records.

## Features

- Create a student record
- List all students and search by name, email, or course
- Retrieve one student by ID
- Update a record with PATCH or replace it with PUT
- Delete a record
- SQLite persistence
- Input validation and useful HTTP error responses
- Interactive API documentation at `/docs`

## Requirements

- Python 3.10 or newer
- Internet connection for installing Python packages

## Run on Windows (VS Code)

1. Extract the ZIP file.
2. Open the extracted `ewb_students_crud` folder in VS Code.
3. Open **Terminal → New Terminal**.
4. Create a virtual environment:

   ```powershell
   py -m venv .venv
   ```

5. Activate it in PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, use Command Prompt and run:

   ```bat
   .venv\Scripts\activate.bat
   ```

6. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

7. Start the API:

   ```powershell
   python -m uvicorn main:app --reload
   ```

8. Open `http://127.0.0.1:8000/docs` in your browser.

The SQLite database file `students.db` is created automatically in the project directory when the app starts.

## Test the endpoints

In `/docs`, expand **POST /students**, choose **Try it out**, and submit example data:

```json
{
  "name": "Demo Student",
  "date_of_birth": "2005-06-15",
  "email": "demo.student@example.com",
  "phone": "9876543210",
  "course": "AI and Machine Learning",
  "address": "Demo City"
}
```

Then test:
- `GET /students` — list records
- `GET /students/1` — retrieve record 1 (use the ID returned by POST)
- `GET /students?search=AI` — search by name, email, or course
- `PATCH /students/1` — update only fields supplied, using the ID returned by POST
- `PUT /students/1` — replace a record with all required fields
- `DELETE /students/1` — delete a record

Use only fictional test data. Do not enter real student personal information.

## Project structure

```text
ewb_students_crud/
├── main.py
├── requirements.txt
├── README.md
└── app/
    ├── __init__.py
    ├── database.py
    ├── models.py
    ├── schemas.py
    └── routes/
        ├── __init__.py
        └── students.py
```

## GitHub submission

1. Create a new **public** GitHub repository, for example `ewb-students-crud-api`.
2. Upload the extracted project files. Do not upload `.venv`, `students.db`, passwords, API keys, or real personal data.
3. Check that `README.md` and `requirements.txt` are present.
4. Copy the repository URL and submit it through the channel announced by your EWB trainer.

## Be ready to explain

- **FastAPI:** defines and serves HTTP API endpoints.
- **SQLite:** stores student records in a local database file.
- **SQLAlchemy:** maps Python objects to database records.
- **Pydantic:** validates incoming request data and shapes responses.
- **CRUD:** Create, Read, Update, Delete.
- **HTTP status codes:** 201 means created, 404 means not found, 409 means conflict, and 204 means successful deletion without a response body.

## Scope

This project implements the mandatory CRUD assignment. The optional Ollama AI extension is not included; EWB's assignment says it is optional.
