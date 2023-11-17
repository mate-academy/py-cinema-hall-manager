from dataclasses import dataclass


@dataclass
class Actor:
    objects = None

    id: int
    first_name: str
    last_name: str
