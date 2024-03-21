from models import Actor
from managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()
    print(Actor.objects.all())
    Actor.objects.create(first_name="Emma", last_name="Watson")
    Actor.objects.create(first_name="Daniel", last_name="Radcliffe")
    Actor.objects.create(first_name="Robert", last_name="Pattinson")
    Actor.objects.create(first_name="John", last_name="Washington")
    Actor.objects.create(first_name="Emma", last_name="Watson")
    print(Actor.objects.all())
    Actor.objects.update(1, "Matthew", "McConaughey")
    Actor.objects.delete(5)
    print(Actor.objects.all())
