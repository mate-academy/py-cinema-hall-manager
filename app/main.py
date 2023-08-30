from models import Actor
from managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()

    Actor.objects.clear()

    Actor.objects.create(first_name="Emma", last_name="Watson")
    Actor.objects.create(first_name="Daniel", last_name="Radclife")
    print("Created:\n", Actor.objects.all())

    Actor.objects.update(2, "Daniel", "Radcliffe@@@@")
    print("\nRadcliffe was updated:\n", Actor.objects.all())

    Actor.objects.delete(1)
    print("\nEmma was deleted:\n", Actor.objects.all())
