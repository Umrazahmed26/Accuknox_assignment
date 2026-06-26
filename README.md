# Accuknox Assignment

A small Django project that demonstrates two assignment topics:

- A custom `Rectangle` class that can be iterated to return its `length` and `width`.
- Notes and proof snippets explaining default Django signal behavior.

The runnable Django app exposes a JSON endpoint for the rectangle iterator example.

## Project Overview

The core implementation lives in `rectangle/rectangleApp/rectangle.py`:

```python
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}
```

Iterating over a `Rectangle(10, 5)` produces:

```python
{'length': 10}
{'width': 5}
```

The Django view in `rectangle/rectangleApp/views.py` returns the same result as JSON.

## Tech Stack

- Python
- Django 6.0.6
- SQLite

## Repository Structure

```text
.
|-- README.md
|-- requirements.txt
|-- Topic_Django Signals
`-- rectangle/
    |-- manage.py
    |-- db.sqlite3
    |-- rectangle/
    |   |-- settings.py
    |   |-- urls.py
    |   |-- asgi.py
    |   `-- wsgi.py
    `-- rectangleApp/
        |-- rectangle.py
        |-- views.py
        |-- urls.py
        |-- models.py
        `-- migrations/
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Rectangle
```

### 2. Create and Activate a Virtual Environment

Windows PowerShell:

```powershell
python -m venv myenv
.\myenv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python -m venv myenv
source myenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
cd rectangle
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

The app will be available at:

```text
http://127.0.0.1:8000/
```

## API Endpoint

### Test Rectangle Iterator

```http
GET /test_rectangle/
```

Example response:

```json
[
  {
    "length": 10
  },
  {
    "width": 5
  }
]
```

This endpoint creates a `Rectangle(10, 5)`, iterates over it, and returns each yielded dictionary in a JSON array.

## Django Signals Notes

The file `Topic_Django Signals` contains written answers and code snippets for these questions:

- Are Django signals synchronous or asynchronous by default?
- Do Django signals run in the same thread as the caller?
- Do Django signals run in the same database transaction as the caller?

Summary:

- Django signals are synchronous by default.
- Django signals run in the same thread as the caller by default.
- Signal handlers run inside the same database transaction as the caller when triggered within an active transaction.

## Current Implementation Notes

- `rectangleApp.models.MyModel` defines a simple model with a `name` field.
- The initial migration also includes a `SignalLog` model, but `SignalLog` is not currently present in `models.py`.
- `rectangleApp/tests.py` is currently empty.
- `rectangleApp/rectangle.py` includes demonstration code at module level, so importing `Rectangle` also prints the sample iteration output in the console.

## Useful Commands

Run the Django development server:

```bash
cd rectangle
python manage.py runserver
```

Run Django checks:

```bash
cd rectangle
python manage.py check
```

Run tests:

```bash
cd rectangle
python manage.py test
```
