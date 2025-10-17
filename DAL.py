import sqlite3
from typing import List, Dict, Optional, Tuple

DB_PATH = "projects.db"


def _get_connection(db_path: str = DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path: str = DB_PATH) -> None:
    conn = _get_connection(db_path)
    try:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                image_file_name TEXT NOT NULL
            )
            """
        )
        conn.commit()
    finally:
        conn.close()


def get_all_projects(db_path: str = DB_PATH) -> List[Dict[str, str]]:
    conn = _get_connection(db_path)
    try:
        rows = conn.execute(
            "SELECT id, title, description, image_file_name FROM projects ORDER BY id DESC"
        ).fetchall()
        return [
            {
                "id": row["id"],
                "title": row["title"],
                "description": row["description"],
                "image_file_name": row["image_file_name"],
            }
            for row in rows
        ]
    finally:
        conn.close()


def insert_project(title: str, description: str, image_file_name: str, db_path: str = DB_PATH) -> int:
    if not title or not description or not image_file_name:
        raise ValueError("title, description, and image_file_name are required")
    conn = _get_connection(db_path)
    try:
        cur = conn.execute(
            "INSERT INTO projects (title, description, image_file_name) VALUES (?, ?, ?)",
            (title.strip(), description.strip(), image_file_name.strip()),
        )
        conn.commit()
        return int(cur.lastrowid)
    finally:
        conn.close()
