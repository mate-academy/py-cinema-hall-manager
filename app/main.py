from managers import ActorManager
from models import Actor

if __name__ == "__main__":
    Actor.objects = ActorManager()

    Actor.objects.create(first_name="Martin", last_name="Watson")
    Actor.objects.create(first_name="Benedict", last_name="Сamembert")
    print(Actor.objects.all())
    Actor.objects.update(2, "Benedict", "Cumberbatch")
    print(Actor.objects.all())
    Actor.objects.delete(1)
    print(Actor.objects.all())
