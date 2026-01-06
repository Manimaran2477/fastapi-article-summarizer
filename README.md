# FastAPI Article Summarizer

## 📌 Problem Understanding & Assumptions

### Problem Understanding
The goal of this project is to build a RESTful backend service using **FastAPI** that manages articles using full **CRUD operations** (Create, Read, Update, Delete).  
The service must persist data in a **PostgreSQL database**, validate input/output strictly using **Pydantic**, and integrate with at least one **external API** before storing or returning data.

### Use Case
**Article Summarization Service**  
A user provides a source URL. The service fetches article content from an external API, generates a short summary, stores the article in the database, and exposes APIs to manage the articles.

### Assumptions
- The external API is publicly accessible and does not require authentication.
- External API responses may fail or return incomplete data.
- User authentication is out of scope.
- Articles are uniquely identified using UUIDs.
- The database is available locally via PostgreSQL.
- Network failures and invalid inputs are expected and handled gracefully.

---

## 🏗️ Design Decisions

### Database Schema
- **articles table**
  - `id` (UUID, Primary Key)
  - `title` (string)
  - `content` (text)
  - `summary` (text)
  - `source_url` (string)

Indexes are applied on the `id` field for fast lookup.

### Project Structure

fastapi-article-summarizer/
│
├── app/
│ ├── main.py # FastAPI app entry point
│ ├── database.py # DB session & engine
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── crud.py # Database operations
│ ├── exceptions.py # Custom exception handling
│ ├── routers/
│ │ └── articles.py # API endpoints
│ └── services/
│ └── external_api.py # External API integration
│
├── tests/ # Pytest test cases
├── .env.example # Environment variables template
├── .gitignore
├── README.md
└── requirements.txt


This follows a **layered architecture** separating API, business logic, and persistence.

### Validation Logic
- All request bodies and responses use **Pydantic models**
- Strict field validation for URLs, strings, and required fields
- Invalid inputs automatically return `422 Unprocessable Entity`

### External API Design
- External API calls are isolated in the `services` layer
- Timeouts and unexpected responses are handled using try/except
- Failures return controlled error responses instead of crashing the app

---

## 🔄 Solution Approach (Data Flow)

1. Client sends a POST request with `source_url`
2. API calls external service to fetch article data
3. Title and content are extracted
4. Summary is generated from content
5. Data is saved in PostgreSQL
6. Response is returned using a Pydantic schema

---

## ⚠️ Error Handling Strategy

- **Database Errors**: Handled using try/except and rolled back safely
- **External API Failures**: Returns meaningful HTTP errors
- **Not Found Resources**: Returns `404 Not Found`
- **Validation Errors**: Handled automatically by FastAPI
- Custom HTTP exceptions are used where appropriate

---

## 🚀 API Endpoints

| Method | Endpoint | Description |
|------|---------|------------|
| POST | `/articles` | Create article |
| GET | `/articles/{article_id}` | Get article |
| PUT | `/articles/{article_id}` | Update article |
| DELETE | `/articles/{article_id}` | Delete article |

Status codes used: `201`, `200`, `204`, `404`, `422`

---

## 🧪 Testing Strategy

### Unit Tests
- CRUD operations
- Schema validation
- Utility functions

### Integration Tests
- API endpoints tested using FastAPI TestClient
- External API calls mocked
- Database interactions tested in isolation

Tests are written using **Pytest**.

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

git clone https://github.com/Manimaran2477/fastapi-article-summarizer.git
cd fastapi-article-summarizer

### 2️⃣ Create Virtual Environment

python -m venv venv
venv\Scripts\activate

### 3️⃣ Install Dependencies

pip install -r requirements.txt

### 4️⃣ Configure Environment Variables

Create a `.env` file using `.env.example` and add:

DATABASE_URL=postgresql://postgres:password@localhost:5432/article_db

### 5️⃣ Start the Server

uvicorn app.main:app --reload

### 6️⃣ Open Swagger UI

http://127.0.0.1:8000/docs


📌 **All these steps are written ONLY in `README.md`**

---

## ❌ WHERE NOT TO WRITE
Do ❌ NOT write these steps in:
- `main.py`
- `database.py`
- Terminal
- Comments in code

They belong **only in documentation (README.md)**.

---

## ✅ AFTER WRITING (MANDATORY)

Once you finish writing steps 2–6 in `README.md`:

```bash
git add README.md
git commit -m "Update run steps in README"
git push origin main




