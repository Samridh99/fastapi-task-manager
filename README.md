# FastAPI Task Manager

This is a FastAPI-based CRUD service for managing tasks, integrated with PostgreSQL and Google Gemini for task categorization.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/fastapi-task-manager.git
   cd fastapi-task-manager
Set up a virtual environment:


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:


pip install -r requirements.txt
Set up environment variables:
Create a .env file in the root directory with the following content:


DATABASE_URL=postgresql://username:password@localhost:5432/taskdb
GEMINI_API_KEY=your_gemini_api_key_here
Run database migrations:


alembic upgrade head
Start the FastAPI server:


uvicorn main:app --reload
API Usage
Create a Task
Endpoint: POST /tasks/

Request Body:

json
Copy
{
  "title": "Fix login button",
  "description": "The login button does not work on mobile devices.",
  "status": false
}
Retrieve a Task
Endpoint: GET /tasks/{task_id}

Update a Task
Endpoint: PUT /tasks/{task_id}

Request Body:

json
Copy
{
  "title": "Fix login button on mobile",
  "status": true
}
Delete a Task
Endpoint: DELETE /tasks/{task_id}

Analyze a Task
Endpoint: POST /tasks/analyze/

Request Body:

json
Copy
{
  "description": "The login button does not work on mobile devices."
}
Response:

json
Copy
{
  "category": "Bug"
}
Assumptions
PostgreSQL is used as the database.

Google Gemini is used for task categorization.

Alembic is used for database migrations.