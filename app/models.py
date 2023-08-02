from dataclasses import dataclass


@dataclass
class Actor:
    id: int
    first_name: str
    last_name: str

    def __repr__(self) -> None:
        return f"Actor #{self.id}: {self.first_name} {self.last_name}"
