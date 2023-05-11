from models import Actor
from managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()

    # Actor.objects.create("Emma", "Watson")
    # Actor.objects.create(first_name="Daniel", last_name="Radclife")
    # print(Actor.objects.all())
    # Actor.objects.update(2, "Daniel", "Radcliffe")
    # print(Actor.objects.all())
    # Actor.objects.delete(4)
    # print(Actor.objects.all())
