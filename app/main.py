from models import Actor
from managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()
    emma = Actor(0, "Emma", "Watson")
    daniel = Actor(0, "Daniel", "Radclife")
    Actor.objects.create(emma)
    Actor.objects.create(daniel)
    print(Actor.objects.all())
    daniel.last_name = "Radcliffe"
    Actor.objects.update(daniel)
    print(Actor.objects.all())
    Actor.objects.delete(1)
    print(Actor.objects.all())
