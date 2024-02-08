from models import Actor
from managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()

    Actor.objects.create(first_name="Anthony", last_name="Hopkins")
    Actor.objects.create(first_name="Brad", last_name="Pitt")
    Actor.objects.create(first_name="Kim", last_name="Kardashian")

    print(Actor.objects.all())
    #  Actor.objects.update(1, "Daniel", "Radcliffe")
    print(Actor.objects.all())
    Actor.objects.delete(7)
    print(Actor.objects.all())
