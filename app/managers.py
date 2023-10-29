from django.db import models


class Actor(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class ActorManager(models.Manager):
    def create_actor(self, first_name: str, last_name: str) -> Actor:
        actor = self.create(first_name=first_name, last_name=last_name)
        return actor

    def update_actor(self, actor_id: int,
                     first_name: str = None, last_name: str = None) -> None:
        actor = self.get(id=actor_id)
        if first_name is not None:
            actor.first_name = first_name
        if last_name is not None:
            actor.last_name = last_name
        actor.save()

    def delete_actor(self, actor_id: int) -> None:
        actor = self.get(id=actor_id)
        actor.delete()
