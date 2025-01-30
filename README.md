FastAPI Task Manager
This is a FastAPI-based CRUD service for managing tasks, integrated with PostgreSQL for data storage and Google Gemini for AI-powered task categorization.

Table of Contents
Features

Setup Instructions

API Usage

Assumptions

Postman Collection

Features
CRUD Operations: Create, Read, Update, and Delete tasks.

AI-Powered Task Categorization: Uses Google Gemini to categorize tasks into "Bug", "Feature Request", or "Improvement".

Database Migrations: Uses Alembic for seamless database schema migrations.

Setup Instructions
Prerequisites
Python 3.9+

PostgreSQL

Google Gemini API Key

Steps
Clone the repository:

bash
Copy
git clone https://github.com/your-username/fastapi-task-manager.git
cd fastapi-task-manager
Set up a virtual environment:

bash
Copy
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
pip install -r requirements.txt
Set up environment variables:
Create a .env file in the root directory with the following content:

plaintext
Copy
DATABASE_URL=postgresql://username:password@localhost:5432/taskdb
GEMINI_API_KEY=your_gemini_api_key_here
Run database migrations:

bash
Copy
alembic upgrade head
Start the FastAPI server:

bash
Copy
uvicorn main:app --reload
API Usage
Tasks
Create a Task:

Endpoint: POST /tasks/

Request Body:

json
Copy
{
  "title": "Fix login button",
  "description": "The login button does not work on mobile devices.",
  "status": false
}
Retrieve a Task:

Endpoint: GET /tasks/{task_id}

Update a Task:

Endpoint: PUT /tasks/{task_id}

Request Body:

json
Copy
{
  "title": "Fix login button on mobile",
  "status": true
}
Delete a Task:

Endpoint: DELETE /tasks/{task_id}

Task Analysis
Analyze a Task:

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

Postman Collection
You can import the Postman collection to test the API endpoints:

Download the Postman collection file: postman_collection.json.

Import the file into Postman.

Use the provided requests to test the API.

Alternatively, use the following cURL commands:

Create a Task
bash
Copy
curl -X POST "http://127.0.0.1:8000/tasks/" -H "Content-Type: application/json" -d '{"title": "Fix login button", "description": "The login button does not work on mobile devices.", "status": false}'
Analyze a Task
bash
Copy
curl -X POST "http://127.0.0.1:8000/tasks/analyze/" -H "Content-Type: application/json" -d '{"description": "The login button does not work on mobile devices."}'
License
This project is licensed under the MIT License. See the LICENSE file for details.