import sqlite3

from backend.database import get_connection


class AdministratorRepository:
    def get_by_username(self, username: str) -> sqlite3.Row | None:
        with get_connection() as connection:
            return connection.execute(
                "SELECT id, username, password_hash "
                "FROM administrators WHERE username = ?",
                (username,),
            ).fetchone()
