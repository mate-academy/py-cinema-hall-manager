# from models import Actor
# from managers import ActorManager
#
# if __name__ == "__main__":
#     Actor.objects = ActorManager()
#
#     Actor.objects.create(first_name="Emma", last_name="Watson")
#     Actor.objects.create(first_name="Daniel", last_name="Radclife")
#     print(Actor.objects.all())
#     Actor.objects.update(2, "Daniel", "Radcliffe")
#     print(Actor.objects.all())
#     Actor.objects.delete(1)
#     print(Actor.objects.all())


from managers import ActorManager

if __name__ == "__main__":
    manager = ActorManager()

    manager.create("Emma", "Watson")
    manager.create("Daniel", "Radcliffe")

    actors = manager.all()
    print("All actors:", actors)

    manager.update(2, "Daniel", "Radcliffe Updated")

    actors = manager.all()
    print("Updated actors:", actors)

    manager.delete(1)

    actors = manager.all()
    print("Actors after deletion:", actors)
