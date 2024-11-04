from dataclasses import dataclass


@dataclass
class Actor:
    "Class Actor with attributes id, first_name and last_name"

    id: int
    first_name: str
    last_name: str
