from managers import ActorManager
from models import Actor

if __name__ == '__main__':
    Actor.objects = ActorManager()

    Actor.objects.create("Oleh", "Boyar")
    Actor.objects.create("Alex", "Bros")
    actors = Actor.objects.all()

    for actor in actors:
        print(actor)

