from dataclasses import dataclass

from app.managers import ActorManager


@dataclass
class Actor:
    objects = ActorManager()
    id: int
    first_name: str
    last_name: str
