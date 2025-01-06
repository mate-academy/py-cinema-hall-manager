from models import Actor
from managers import ActorManager


if __name__ == "__main__":
    Actor.objects = ActorManager()

    Actor.objects.create(first_name="Selena", last_name="Gomes")
    Actor.objects.create(first_name="Tom", last_name="Holland")
    print(Actor.objects.all())
    Actor.objects.update(2, "Daniel", "Radcliffe")
    print(Actor.objects.all())
    Actor.objects.delete(12)
    print(Actor.objects.all())
