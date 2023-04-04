from dataclasses import dataclass


@dataclass
class Actor:
    """A class to create actor"""
    id: int
    first_name: str
    last_name: str
