from models import Actor
from managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()

    Actor.objects.create(actor_first_name="Kyree", actor_last_name="Alexander")
    Actor.objects.create(actor_first_name="Toni", actor_last_name="Alonzo")
    Actor.objects.create(actor_first_name="Peter", actor_last_name="Armstrong")
    Actor.objects.create(actor_first_name="Daniel", actor_last_name="Baker")
    Actor.objects.create(actor_first_name="Cassie", actor_last_name="Parsons")
    print(Actor.objects.all())
    Actor.objects.update(13, "Paige", "Peterson")
    print(Actor.objects.all())
    Actor.objects.delete(13)
    print(Actor.objects.all())
