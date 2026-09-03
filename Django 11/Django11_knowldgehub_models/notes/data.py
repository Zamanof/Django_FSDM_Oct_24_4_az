from copy import deepcopy
from datetime import datetime
from typing import Any

from typing import Any

_NOTES: list[dict[str, Any]] = [
    {
        "id": 1,
        "title": "Django Views",
        "content": "Views accept a request and return a response.",
        "tags": ["python", "django"],
        "category": "backend",
        "created_at": datetime(2026, 8, 24)
    },
    {
        "id": 2,
        "title": "Django Models",
        "content": "Models are used to work with data and databases.",
        "tags": ["python", "django", "database"],
        "category": "backend",
        "created_at": datetime(2026, 8, 23)
    },
    {
        "id": 3,
        "title": "Django Templates",
        "content": "Templates are used to generate dynamic HTML pages.",
        "tags": ["django", "html"],
        "category": "frontend",
        "created_at": datetime(2026, 8, 22)
    },
    {
        "id": 4,
        "title": "Django URLs",
        "content": "URL patterns connect URLs with Django views.",
        "tags": ["python", "django", "routing"],
        "category": "backend",
        "created_at": datetime(2026, 8, 21)
    },
    {
        "id": 5,
        "title": "Python Functions",
        "content": "Functions allow us to organize and reuse code.",
        "tags": ["python", "functions"],
        "category": "python",
        "created_at": datetime(2026, 8, 20)
    },
    {
        "id": 6,
        "title": "HTML Forms",
        "content": "HTML forms are used to collect data from users.",
        "tags": ["html", "forms"],
        "category": "frontend",
        "created_at": datetime(2026, 8, 19)
    },
    {
        "id": 7,
        "title": "Django Forms",
        "content": "Django Forms simplify validation and processing of user input.",
        "tags": ["python", "django", "forms"],
        "category": "backend",
        "created_at": datetime(2026, 8, 18)
    },
    {
        "id": 8,
        "title": "CSS Basics",
        "content": "CSS is used to style HTML elements.",
        "tags": ["css", "html"],
        "category": "frontend",
        "created_at": datetime(2026, 8, 17)
    },
    {
        "id": 9,
        "title": "Django Static Files",
        "content": "Static files include CSS, JavaScript, images, and other assets.",
        "tags": ["django", "css", "javascript"],
        "category": "frontend",
        "created_at": datetime(2026, 8, 16)
    },
    {
        "id": 10,
        "title": "Django Middleware",
        "content": "Middleware processes requests and responses globally.",
        "tags": ["python", "django", "middleware"],
        "category": "backend",
        "created_at": datetime(2026, 8, 15)
    },
]

_next_id = 11

def list_notes()->list[dict[str, Any]]:
    return deepcopy(_NOTES)


def get_note(note_id:int)-> dict[str, Any] | None:
    for note in _NOTES:
        if note["id"] == note_id:
            return deepcopy(note)
    return None


def create_note(*, title:str, content:str, tags:list[str], category:str)-> dict[str, Any]:
    global _next_id
    note = {
        "id": _next_id,
        "title": title.strip(),
        "content": content.strip(),
        "tags": list(tags),
        "category": category.strip()
    }
    print(note['tags'])
    _NOTES.append(note)
    _next_id += 1
    return deepcopy(note)


def update_note(
        note_id:int,
        *,
        title:str,
        content:str,
        tags:list['str'],
        category:str,
)-> dict[str, Any] | None:
    for note in _NOTES:
        if note["id"] == note_id:
            note["title"] = title.strip()
            note["content"] = content.strip()
            note["category"] = category.strip()
            note["tags"] = list(tags)
            return deepcopy(note)
    return None


def delete_note(note_id:int)-> bool:
    global _NOTES
    before = len(_NOTES)
    _NOTES = [n for n in _NOTES if n["id"] != note_id]
    return len(_NOTES) != before