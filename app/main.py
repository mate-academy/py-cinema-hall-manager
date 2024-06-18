from managers import ActorManager


def main() -> None:
    manager = ActorManager()

    # creations actor
    actor_id1 = manager.create("Роберт", "Дауні-молодший")
    actor_id2 = manager.create("Кріс", "Гемсворт")

    # list  all actors
    actors = manager.all()
    print("Всі актори:")
    for actor in actors:
        print(actor)

    # update actor
    manager.update(actor_id1, first_name="Роберт", last_name="Дауні")
    updated_actors = manager.all()
    print("\nОновлений актор:")
    for actor in updated_actors:
        print(actor)

    # delete actor
    manager.delete(actor_id2)
    remaining_actors = manager.all()
    print("\nЗалишилися актори після видалення:")
    for actor in remaining_actors:
        print(actor)


if __name__ == "__main__":
    main()
