import sqlite3

from backend.database import get_connection


class PeopleRepository:
    def get_all(self) -> list[sqlite3.Row]:
        with get_connection() as connection:
            return connection.execute(
                "SELECT id, full_name, permission FROM people ORDER BY id"
            ).fetchall()

    def get_by_id(self, person_id: int) -> sqlite3.Row | None:
        with get_connection() as connection:
            return connection.execute(
                "SELECT id, full_name, permission FROM people WHERE id = ?",
                (person_id,),
            ).fetchone()

    def create(self, full_name: str, permission: str) -> int:
        with get_connection() as connection:
            cursor = connection.execute(
                "INSERT INTO people (full_name, permission) VALUES (?, ?)",
                (full_name, permission),
            )
            return int(cursor.lastrowid)

    def delete(self, person_id: int) -> bool:
        with get_connection() as connection:
            cursor = connection.execute(
                "DELETE FROM people WHERE id = ?",
                (person_id,),
            )
            return cursor.rowcount > 0
