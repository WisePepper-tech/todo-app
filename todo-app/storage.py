import json
from typing import List
from todo import Task

FILE_NAME = "tasks.json"


def load_tasks():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [Task(**item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks: List[Task]) -> None:
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump([task.__dict__ for task in tasks], file, indent=2, ensure_ascii=False)
