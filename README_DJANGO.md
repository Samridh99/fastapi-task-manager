# Django Task Manager

This is a **Django-based task management web application** converted from FastAPI, featuring AI-powered task categorization with **Google Gemini**, **PostgreSQL** database integration, and a modern responsive web interface with dark mode support.

![Task Manager Dashboard](https://github.com/user-attachments/assets/67f2423f-2925-434f-94ec-e64499178ee6)

![Dark Mode](https://github.com/user-attachments/assets/d4397b99-d227-436d-a558-03d7a1e0c253)

## ✨ Features

### Core Functionality
- **Complete Task CRUD Operations**: Create, Read, Update, and Delete tasks
- **AI-Powered Task Categorization**: Uses Google Gemini to automatically categorize tasks into *"Bug"*, *"Feature Request"*, or *"Improvement"*
- **Real-time Dashboard**: Interactive web interface with live statistics and task management
- **Dark/Light Mode Toggle**: Switch between themes with persistent preference storage
- **Responsive Design**: Mobile-friendly interface using Tailwind CSS

### Technical Features
- **Django REST API**: RESTful endpoints equivalent to the original FastAPI implementation
- **PostgreSQL Integration**: Production-ready database with Django ORM
- **Django Admin Interface**: Built-in administrative interface for task management
- **Management Commands**: Custom Django commands for database seeding and operations
- **Modern Frontend**: Responsive UI with AJAX interactions and real-time updates

## 🏗️ Architecture

### Converted Components

| Original FastAPI | Django Equivalent | Description |
|------------------|-------------------|-------------|
| `main.py` | `tasks/views.py` | API endpoints and view logic |
| `models.py` (SQLAlchemy) | `tasks/models.py` | Django ORM models |
| `analyzer.py` | `analysis/services.py` | AI analysis service |
| Pydantic models | `tasks/serializers.py` | DRF serializers |
| Alembic migrations | Django migrations | Database schema management |

### Project Structure
```
task_manager_django/
├── task_manager_django/     # Django project settings
│   ├── settings.py         # Configuration and database setup
│   ├── urls.py            # Main URL routing
│   └── wsgi.py            # WSGI application
├── tasks/                  # Main tasks application
│   ├── models.py          # Task model (Django ORM)
│   ├── views.py           # API views and dashboard
│   ├── serializers.py     # DRF serializers
│   ├── urls.py            # Task URL routing
│   ├── admin.py           # Django admin configuration
│   └── management/        # Custom management commands
│       └── commands/
│           └── seed_tasks.py
├── analysis/               # AI analysis service
│   └── services.py        # Gemini integration
├── templates/              # HTML templates
│   ├── base.html          # Base template with navigation
│   └── task_list.html     # Dashboard interface
└── static/                 # Static files directory
```

## 🚀 Setup Instructions

### Prerequisites
- Python 3.9+
- PostgreSQL database
- Google Gemini API Key (for AI features)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd fastapi-task-manager
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Django dependencies**:
   ```bash
   pip install -r requirements_django.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```env
   # Database Configuration
   DATABASE_URL=postgresql://username:password@localhost:5432/taskdb
   
   # AI Features (optional - will gracefully degrade without it)
   GEMINI_API_KEY=your_gemini_api_key_here
   
   # Django Settings
   DEBUG=True
   SECRET_KEY=your-secret-key-here
   ```

5. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Seed sample data** (optional):
   ```bash
   python manage.py seed_tasks
   ```

7. **Create admin user** (optional):
   ```bash
   python manage.py createsuperuser
   ```

8. **Start the Django development server**:
   ```bash
   python manage.py runserver
   ```

The application will be available at:
- **Dashboard**: http://127.0.0.1:8000/ (main interface)
- **API Root**: http://127.0.0.1:8000/tasks/ (REST API)
- **Admin Panel**: http://127.0.0.1:8000/admin/ (Django admin)

## 📚 API Documentation

### Task Management Endpoints

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| `GET` | `/tasks/` | List all tasks | - |
| `POST` | `/tasks/` | Create new task | `{"title": "string", "description": "string", "status": boolean}` |
| `GET` | `/tasks/{id}/` | Get specific task | - |
| `PUT` | `/tasks/{id}/` | Update task | `{"title": "string", "description": "string", "status": boolean}` |
| `DELETE` | `/tasks/{id}/` | Delete task | - |
| `POST` | `/tasks/analyze/` | Analyze task with AI | `{"description": "string"}` |

### Example Usage

**Create a Task**:
```bash
curl -X POST "http://127.0.0.1:8000/tasks/" \
  -H "Content-Type: application/json" \
  -d '{"title": "Fix login issue", "description": "Login button not working on mobile", "status": false}'
```

**Analyze a Task**:
```bash
curl -X POST "http://127.0.0.1:8000/tasks/analyze/" \
  -H "Content-Type: application/json" \
  -d '{"description": "The login button does not work on mobile devices"}'
```

Response:
```json
{"category": "Bug"}
```

## 🎯 Key Features Demo

### Dashboard Interface
- **Task Statistics**: Real-time counters for total, completed, and pending tasks
- **Task List**: Interactive list with inline actions (edit, delete, analyze)
- **Dark Mode**: Toggle between light and dark themes
- **Responsive Design**: Works on desktop, tablet, and mobile devices

### AI-Powered Analysis
Tasks can be automatically categorized using Google Gemini:
- **Bug**: Issues that need fixing
- **Feature Request**: New functionality requests  
- **Improvement**: Enhancements to existing features
- **Uncategorized**: Fallback for unclear descriptions

### Admin Interface
Access the Django admin at `/admin/` to:
- Manage tasks with advanced filtering and search
- Bulk operations on multiple tasks
- User and permission management
- Database insights and maintenance

## 🛠️ Management Commands

### Seed Database
```bash
# Add sample tasks
python manage.py seed_tasks

# Clear existing tasks and add sample data
python manage.py seed_tasks --clear
```

### Database Operations
```bash
# Create migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser
```

## 🔄 Migration from FastAPI

This Django application maintains **100% functional compatibility** with the original FastAPI version:

### ✅ Preserved Features
- All CRUD operations work identically
- Same API request/response formats
- Identical AI analysis functionality
- Same database schema (compatible with existing data)
- All original endpoints accessible at same paths

### ✨ Enhanced Features
- **Web Interface**: Modern dashboard instead of just API
- **Admin Panel**: Built-in administrative interface
- **Better ORM**: Django ORM with advanced querying capabilities
- **Management Commands**: Easy database operations and maintenance
- **Template System**: Server-side rendering for better SEO and performance

### 📦 Deployment Ready
- **WSGI Compatible**: Deploy with Gunicorn, uWSGI, or mod_wsgi
- **Static Files**: Proper static file handling for production
- **Settings Management**: Environment-based configuration
- **Security**: Django's built-in security features enabled

## 🧪 Testing

The application can be tested using the same methods as the original FastAPI version:

```bash
# Test API endpoints
curl -X GET "http://127.0.0.1:8000/tasks/"
curl -X POST "http://127.0.0.1:8000/tasks/" -H "Content-Type: application/json" -d '{"title": "Test Task", "description": "Test description"}'

# Test web interface
# Open http://127.0.0.1:8000/ in your browser
```

## 📈 Performance Notes

- **Database**: Uses Django ORM with optimized queries
- **Frontend**: Single-page application with AJAX for smooth interactions
- **Static Files**: Served efficiently with proper caching headers
- **API**: DRF provides excellent performance for REST operations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and ensure functionality
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

**Note**: This Django application is a complete conversion from the original FastAPI implementation, providing the same functionality with additional web interface capabilities and Django ecosystem benefits.