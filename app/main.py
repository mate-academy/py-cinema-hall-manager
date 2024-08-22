from managers import ActorManager

if __name__ == "__main__":
    manager = ActorManager()

    manager.create("Emma", "Watson")
    manager.create("Daniel", "Radcliffe")
    print(manager.all())
    manager.update(2, "Daniel", "Radcliffe")
    print(manager.all())
    manager.delete(1)
    print(manager.all())
