from models import Actor
from managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()

    Actor.objects.create(first_name="Tom", last_name="Henks")
    Actor.objects.create(first_name="Tina", last_name="Brauni")
    print(Actor.objects.all())
    Actor.objects.delete(1)
    print(Actor.objects.all())
