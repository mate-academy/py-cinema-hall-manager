from dataclasses import dataclass


@dataclass
class Actor:
    id: int
    first_name: str
    last_name: str

    def __repr__(self):
        return f"Actor #{self.id}: {self.first_name} {self.last_name}"


if __name__ == '__main__':
    example = Actor(id=321, first_name="Fn", last_name="Ln")
    print(example)
