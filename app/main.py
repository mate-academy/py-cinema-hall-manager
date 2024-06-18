from models import Actor
from managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()

    Actor.objects.create(first_name="Eric", last_name="Cartman")
    Actor.objects.create(first_name="Megan", last_name="First")
    print(Actor.objects.all())
    Actor.objects.update(2, "Mariy", "Crash")
    print(Actor.objects.all())
    Actor.objects.delete(1)
    print(Actor.objects.all())
