from dataclasses import dataclass


@dataclass
class Actor:
    id: int
    first_name: str
    last_name: str

    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name}"
