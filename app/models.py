from dataclasses import dataclass


@dataclass
class Actor:
    user_id: int
    first_name: str
    last_name: str
