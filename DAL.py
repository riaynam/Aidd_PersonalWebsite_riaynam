import sqlite3
from pathlib import Path
from typing import List, Dict, Optional

DB_PATH = Path(__file__).parent / "projects.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                imageFileName TEXT
            )
            """
        )

def insert_project(title: str, description: str, imageFileName: Optional[str] = None) -> int:
    with get_connection() as conn:
        cur = conn.execute(
            "INSERT INTO projects (title, description, imageFileName) VALUES (?, ?, ?)",
            (title, description, imageFileName),
        )
        return cur.lastrowid

def get_projects() -> List[Dict]:
    with get_connection() as conn:
        cur = conn.execute("SELECT id, title, description, imageFileName FROM projects ORDER BY id DESC")
        rows = cur.fetchall()
        return [dict(r) for r in rows]

def get_project(project_id: int) -> Optional[Dict]:
    with get_connection() as conn:
        cur = conn.execute("SELECT id, title, description, imageFileName FROM projects WHERE id = ?", (project_id,))
        row = cur.fetchone()
        return dict(row) if row else None
