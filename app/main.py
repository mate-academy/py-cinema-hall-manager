from models import Actor
from managers import ActorFormatManagers


if __name__ == "__main__":
    Actor.objects = ActorFormatManagers()
    Actor.objects.create("Tom", "Backer")
    Actor.objects.create("Sam", "Cooker")
    print(Actor.objects.all())
    Actor.objects.update(2, "Alfred", "Goos")
    print(Actor.objects.all())
    Actor.objects.delete(1)
    print(Actor.objects.all())
