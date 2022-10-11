from app.models import Actor
from app.managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()

    # Actor.objects.create(first_name="Victor", last_name="Pavlik")
    # Actor.objects.create(first_name="Daniel", last_name="Radclife")
    # print(Actor.objects.all())
    # Actor.objects.update(4, "Slavik", "Des")
    # print(Actor.objects.all())
    # Actor.objects.delete(2)
    # print(Actor.objects.all())
