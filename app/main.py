from app.models import Actor
from app.managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()

    # Create new actors
    Actor.objects.create(first_name="Emma", last_name="Watson")
    Actor.objects.create(first_name="Daniel", last_name="Radclife")

    # Get all actors
    print(Actor.objects.all())

    # Update actor's data
    Actor.objects.update(2, "Daniel", "Radcliffe")
    print(Actor.objects.all())

    # Delete an actor
    Actor.objects.delete(1)
    print(Actor.objects.all())
