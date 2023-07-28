from models import Actor
from managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()

    Actor.objects.create(first_name="Emma", last_name="Watson")
    Actor.objects.create(first_name="Daniel", last_name="Radclife")
    print(Actor.objects.all())
    Actor.objects.update(
        id_to_update=2,
        new_first_name="Daniel",
        new_last_name="Radcliffe"
    )
    print(Actor.objects.all())
    Actor.objects.delete(id_to_delete=1)
    print(Actor.objects.all())
