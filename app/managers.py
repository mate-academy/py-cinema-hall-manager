from django.db import models


class ActorManager(models.Manager):
    def create_actor(self, first_name, last_name):
        actor = self.create(first_name=first_name, last_name=last_name)
        return actor

    def update_actor(self, actor_id, first_name=None, last_name=None):
        actor = self.get(id=actor_id)
        if first_name is not None:
            actor.first_name = first_name
        if last_name is not None:
            actor.last_name = last_name
        actor.save()

    def delete_actor(self, actor_id):
        actor = self.get(id=actor_id)
        actor.delete()
