from managers import ActorManagers
from models import Actor


if __name__ == '__main__':
    Actor.objects =ActorManagers()
    print(Actor.objects.all())

