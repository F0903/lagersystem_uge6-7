from ..db_connection import DbConnection
from ...models.user import User


class UserAdapter:

    def __init__(self, db: DbConnection) -> None:
        self._db = db

    def get_user_by_username(self, username: str) -> User | None:
        with self._db.get_cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM users WHERE Username = %s", (username,))

            user_row = cursor.fetchone()
            if not user_row:
                return None

            user = User(
                ID=user_row["ID"],
                Username=user_row["Username"],
                PasswordHash=user_row["PasswordHash"],
                IsAdmin=user_row["Admin"],
            )

            return user
