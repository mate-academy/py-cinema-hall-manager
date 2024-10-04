from managers import ActorManager


if __name__ == "__main__":
    manager = ActorManager()

    manager.create(first_name="Emma", last_name="Watson")
    manager.create(first_name="Daniel", last_name="Radcliffe")

    print("All actors after creation:")
    actors = manager.all()
    for actor in actors:
        print(f"ID: {actor.id}, Name: {actor.first_name} {actor.last_name}")

    print("\nUpdating actor with ID 2 (Daniel Radcliffe)...")
    manager.update(2, "Daniel", "Radcliffe")

    print("\nAll actors after update:")
    actors = manager.all()
    for actor in actors:
        print(f"ID: {actor.id}, Name: {actor.first_name} {actor.last_name}")

    print("\nDeleting actor with ID 1 (Emma Watson)...")
    manager.delete(1)

    print("\nAll actors after deletion:")
    actors = manager.all()
    for actor in actors:
        print(f"ID: {actor.id}, Name: {actor.first_name} {actor.last_name}")
