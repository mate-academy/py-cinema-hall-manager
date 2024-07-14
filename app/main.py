from managers import ActorManager


def main() -> None:
    manager = ActorManager()

    manager.create("Leonardo", "DiCaprio")
    manager.create("Morgan", "Freeman")

    actors = manager.all()
    print("Actors in database:")
    for actor in actors:
        print(actor)

    manager.update(1, new_first_name="Leonard", new_last_name="DiCaprio")

    manager.delete(2)

    actors = manager.all()
    print("Actors in database after update and delete:")
    for actor in actors:
        print(actor)


if __name__ == "__main__":
    main()
