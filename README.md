# FAQ Management System with Multi-Language Support

A Django-based system for managing FAQs with WYSIWYG editing, automatic translations, and REST API support.  
**Key Features**:
- 📝 Rich text editor for FAQ answers
- 🌐 Multi-language support with automated translations
- ⚡ Redis caching for high performance
- 🔧 Admin interface for content management
- 📡 REST API with language parameter support

---

## Table of Contents
1. [Installation](#1-installation)
2. [API Documentation](#2-api-documentation)
3. [System Features](#3-system-features)
4. [Admin Panel](#4-admin-panel)
5. [Testing](#5-testing)
6. [Configuration](#6-configuration)
7. [License](#7-license)

---

## 1. Installation

### Prerequisites
- Python 3.8+
- Redis server

### Setup Steps
1. **Clone Repository**
   ```bash
   git clone https://github.com/yourusername/faq-system.git
   cd faq-system
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**
   ```bash
   python manage.py migrate
   ```

5. **Create Admin User**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

---

## 2. API Documentation

### Base URL: `http://localhost:8000/api/faqs/`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/`      | GET    | List all FAQs |
| `/?lang=<code>` | GET | Get translated FAQs (e.g. `?lang=hi`) |
| `/`      | POST   | Create new FAQ |

### Example Requests

**Get English FAQs**
```bash
curl http://localhost:8000/api/faqs/
```

**Get Hindi Translations**
```bash
curl http://localhost:8000/api/faqs/?lang=hi
```

**Create New FAQ**
```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
  "question": "How to use API?",
  "answer": "Use HTTP methods...",
  "question_hi": "API का उपयोग कैसे करें?",
  "answer_hi": "HTTP विधियों का प्रयोग..."
}' \
http://localhost:8000/api/faqs/
```

---

## 3. System Features

### Multi-Language Support
- **Supported Languages**: Hindi (`hi`), Bengali (`bn`), English (`en`)
- **Automatic Translation**: Uses Google Translate API during object creation
- **Fallback System**: Returns English content if translation missing

### Caching Mechanism
- **Redis Integration**: Caches API responses for 1 hour
- **Cache Invalidation**: Automatic refresh on FAQ updates
- **Key Structure**: `faq:<language_code>:<version>`

### WYSIWYG Editor
- **CKEditor Features**:
  - Text formatting
  - Lists
  - HTML editing
  - Multi-language content support

---

## 4. Admin Panel

Access at `http://localhost:8000/admin/`

**Key Admin Features**:
- Rich text editor for answers
- Translation management interface
- Search/filter by question or language
- Bulk actions for FAQs


---

## 5. Testing

Run the test suite with:
```bash
pytest tests/ --cov
```

**Test Coverage**:
- Model methods
- API endpoints
- Translation logic
- Cache operations

---

## 6. Configuration


### Customizing Languages
1. Edit `settings.py`:
   ```python
   SUPPORTED_LANGUAGES = ['en', 'hi', 'bn']  # Add new language codes
   ```

2. Run migrations after adding new fields:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

---

## 7. License

MIT License - See [LICENSE](LICENSE) for details.
```
