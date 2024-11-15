from dataclasses import dataclass
import datetime
from typing import Any, Self


@dataclass(kw_only=True)
class DbItemDescriptor:
    """
    Dataclass that holds the most basic information about every product.
    """

    ID: int
    Type: str
    CreatedAt: datetime.datetime
    LastUpdatedAt: datetime.datetime

    @classmethod
    def create_from_dict(cls, dict: dict[str, Any]) -> Self:
        """
        Factory method for creating a ProductDescriptor from a dictionary.
        """

        descriptor = cls(
            ID=dict["ID"],
            Type=dict["Type"],
            CreatedAt=dict["CreatedAt"],
            LastUpdatedAt=dict["LastUpdatedAt"],
        )
        return descriptor
