from models import Actor
from managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()

    Actor.objects.create_table(first_name="Emma", last_name="Watson")
    Actor.objects.create_table(first_name="Daniel", last_name="Radclife")
    print(Actor.objects.read_table())
    Actor.objects.update_actor(2, "Daniel", "Radcliffe")
    print(Actor.objects.read_table())
    Actor.objects.delete_actor(1)
    print(Actor.objects.read_table())
