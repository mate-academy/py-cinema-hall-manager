from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Actor:
    id: int
    first_name: str
    last_name: str

    objects: ClassVar = None
