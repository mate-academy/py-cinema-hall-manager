from dataclasses import dataclass

from app.managers import ActorManager
from app.models import Actor


@dataclass
class ActorsController:
    manager: ActorManager = ActorManager()
    actor: Actor = Actor

    def table(self) -> ActorManager:
        self.actor.objects = self.manager
        return self.actor.objects
