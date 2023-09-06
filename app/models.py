from dataclasses import dataclass


@dataclass
class Actor:
    id: int  # primary key
    first_name: str
    last_name: str
