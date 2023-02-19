from dataclasses import dataclass

from app.managers import ActorManager


@dataclass
class Actor:
    id: int
    first_name: str
    last_name: str

    objects = ActorManager()
