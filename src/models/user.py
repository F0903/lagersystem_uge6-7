from dataclasses import dataclass
from hashlib import sha256


@dataclass(kw_only=True)
class User:
    ID: int
    Username: str
    PasswordHash: str
    IsAdmin: bool

    def is_password_match(self, plain_password: str) -> bool:
        hashed_password = sha256(plain_password.encode("utf-8")).hexdigest()
        return self.PasswordHash == hashed_password
