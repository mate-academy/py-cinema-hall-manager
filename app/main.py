from models import Actor
from managers import ActorManager


if __name__ == "__main__":
    Actor.objects = ActorManager()
    print(Actor.objects.all())
    Actor.objects.delete(3)
    Actor.objects.update(4, "Maria", "Roberts")
    Actor.objects.create("Maria", "Brown")
    Actor.objects.create("Olena", "Evans")
    Actor.objects.create("Roman", "Wilson")
    print((Actor.objects.all()))
