from models import Actor
from managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()

    Actor.objects.create(input_first_name="Emma", input_last_name="Watson")
    Actor.objects.create(input_first_name="Daniel", input_last_name="Radclife")
    print(Actor.objects.all())
    Actor.objects.update(2, "Daniel", "Radcliffe")
    print(Actor.objects.all())
    Actor.objects.delete(1)
    print(Actor.objects.all())
