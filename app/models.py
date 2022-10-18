from dataclasses import dataclass

from managers import ActorManager


@dataclass
class Actor:
    object = ActorManager()

    id: int
    first_name: str
    last_name: str
