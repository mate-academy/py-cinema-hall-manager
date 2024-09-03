from models import Actor
from manager import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()

    Actor.objects.create(first_name="Walter", last_name="White")
    Actor.objects.create(first_name="Jessy", last_name="Pinkman")
    print(Actor.objects.all())
    Actor.objects.update(2, "Gustavo", "Fring")
    print(Actor.objects.all())
    Actor.objects.delete(1)
    print(Actor.objects.all())
