from copy import deepcopy
from typing import Any

_NOTES: list[dict[str, Any]] = [
    {"id": 1, "title":"First Note", "body":"My First Note Text"},
    {"id": 2, "title":"Second Note", "body":"My Second Note Text"},
]

def list_notes()->list[dict[str, Any]]:
    return deepcopy(_NOTES)


def get_note(note_id:int)-> dict[str, Any] | None:
    for note in _NOTES:
        if note["id"] == note_id:
            return deepcopy(note)
    return None