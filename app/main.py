from models import Actor
from managers import ActorManager


if __name__ == "__main__":
    Actor.objects = ActorManager()

    Actor.objects.create(first_name="Emma", last_name="Watson")
    Actor.objects.create(first_name="Daniel", last_name="Radclife")
    print(Actor.objects.all())
    print(Actor.objects.get(2))
    Actor.objects.update(2, "Denzel", "Washington")
    print(Actor.objects.get(2))
    print(Actor.objects.all())
    Actor.objects.delete(1)
    print(Actor.objects.all())
