# FastAPI Task Manager

This is a **FastAPI-based CRUD service** for managing tasks, integrated with **PostgreSQL** for data storage and **Google Gemini** for AI-powered task categorization.

## Table of Contents
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [API Usage](#api-usage)
- [Assumptions](#assumptions)
- [Postman Collection](#postman-collection)

## Features

- **CRUD Operations**: Create, Read, Update, and Delete tasks.
- **AI-Powered Task Categorization**: Uses Google Gemini to categorize tasks into *"Bug"*, *"Feature Request"*, or *"Improvement"*.
- **Database Migrations**: Uses Alembic for seamless database schema migrations.

---

## Setup Instructions

### Prerequisites
- Python 3.9+
- PostgreSQL
- Google Gemini API Key

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/fastapi-task-manager.git
    cd fastapi-task-manager
    ```

2. **Set up a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory with the following content:
    ```plaintext
    DATABASE_URL=postgresql://username:password@localhost:5432/taskdb
    GEMINI_API_KEY=your_gemini_api_key_here
    ```

5. **Run database migrations**:
    ```bash
    alembic upgrade head
    ```

6. **Start the FastAPI server**:
    ```bash
    uvicorn main:app --reload
    ```

---

## API Usage

### Tasks

- **Create a Task**  
  **Endpoint**: `POST /tasks/`

  **Request Body**:
    ```json
    {
      "title": "Fix login button",
      "description": "The login button does not work on mobile devices.",
      "status": false
    }
    ```

- **Retrieve a Task**  
  **Endpoint**: `GET /tasks/{task_id}`

- **Update a Task**  
  **Endpoint**: `PUT /tasks/{task_id}`

  **Request Body**:
    ```json
    {
      "title": "Fix login button on mobile",
      "status": true
    }
    ```

- **Delete a Task**  
  **Endpoint**: `DELETE /tasks/{task_id}`

### Task Analysis

- **Analyze a Task**  
  **Endpoint**: `POST /tasks/analyze/`

  **Request Body**:
    ```json
    {
      "description": "The login button does not work on mobile devices."
    }
    ```

  **Response**:
    ```json
    {
      "category": "Bug"
    }
    ```

---

## Assumptions

- PostgreSQL is used as the database.
- Google Gemini is used for task categorization.
- Alembic is used for database migrations.

---

## Postman Collection

You can import the **Postman collection** to test the API endpoints:

1. **Download the Postman collection file**: `postman_collection.json`.
2. **Import the file** into Postman.
3. Use the provided requests to test the API.

Alternatively, use the following **cURL commands**:

- **Create a Task**:
    ```bash
    curl -X POST "http://127.0.0.1:8000/tasks/" -H "Content-Type: application/json" -d '{"title": "Fix login button", "description": "The login button does not work on mobile devices.", "status": false}'
    ```

- **Analyze a Task**:
    ```bash
    curl -X POST "http://127.0.0.1:8000/tasks/analyze/" -H "Content-Type: application/json" -d '{"description": "The login button does not work on mobile devices."}'
    ```

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
