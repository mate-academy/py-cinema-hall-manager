import string
from dataclasses import dataclass


@dataclass
class Actor:
    id: int
    first_name: string
    last_name: string
