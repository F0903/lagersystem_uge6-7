from ..db_connection import DbConnection
from ...models.user import User


class UserAdapter:

    def __init__(self, db: DbConnection) -> None:
        self._db = db

    def get_user_by_username(self, username: str) -> User:
        with self._db.get_cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE Username = %s", (username,))

            user_row = cursor.fetchone()
            user = User(
                ID=user_row["ID"],
                Username=user_row["Username"],
                PasswordHash=user_row["PasswordHash"],
                IsAdmin=user_row("Admin"),
            )

            return user
