from dataclasses import dataclass


@dataclass
class Actor:
    id: int
    first_name: str
    last_name: str

    def __repr__(self):
        return f"Actor(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}')"

