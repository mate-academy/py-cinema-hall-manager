from dataclasses import dataclass


@dataclass
class Actor:
    id: int
    first_name: str
    last_name: str

    def __str__(self) -> str:
        return f"{self.id} {self.first_name} {self.last_name}"
