# main.py
from managers import ActorManager


def main() -> None:
    manager = ActorManager()

    # Create new actors
    actor1_id = manager.create("Robert", "Downey Jr.")
    actor2_id = manager.create("Scarlett", "Johansson")
    print(f"Created Actor IDs: {actor1_id}, {actor2_id}")

    # Retrieve all actors
    all_actors = manager.all()
    print("All Actors:", all_actors)

    # Update an actor
    manager.update(actor1_id, first_name="Bob")
    updated_actors = manager.all()
    print("Updated Actors:", updated_actors)

    # Delete an actor
    manager.delete(actor2_id)
    remaining_actors = manager.all()
    print("Remaining Actors:", remaining_actors)


if __name__ == "__main__":
    main()
