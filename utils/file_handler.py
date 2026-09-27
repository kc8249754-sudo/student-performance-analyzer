"""JSON persistence helpers for student records."""

import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "students.json"


def load_students(file_path: str | Path = DATA_FILE) -> list[dict]:
    """Load a list of records; initialize safely if the file is absent/invalid."""
    path = Path(file_path)
    if not path.exists():
        save_students([], path)
        return []
    try:
        with path.open("r", encoding="utf-8") as data_file:
            records = json.load(data_file)
        if not isinstance(records, list) or not all(isinstance(item, dict) for item in records):
            raise ValueError("The JSON root must be a list of student records.")
        return records
    except (json.JSONDecodeError, OSError, ValueError) as error:
        print(f"Could not read {path}: {error} Starting with an empty student list.")
        return []


def save_students(records: list[dict], file_path: str | Path = DATA_FILE) -> None:
    """Save records as readable JSON, creating the parent directory as needed."""
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as data_file:
        json.dump(records, data_file, indent=4, ensure_ascii=False)
