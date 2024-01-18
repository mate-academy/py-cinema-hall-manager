from models import Actor
from managers import ActorManager

if __name__ == "__main__":
    actor_manager = ActorManager()
    actor1 = Actor(id=1, first_name="John", last_name="Doe")
    actor_manager.create(actor1)
    actors_list = actor_manager.all()
    print("All actors:", actors_list)
    actor_manager.update(actor_id=1,
                         new_first_name="Johnny",
                         new_last_name="Doeman")
    updated_actors_list = actor_manager.all()
    print("Updated actors:", updated_actors_list)
    actor_manager.delete(actor_id=1)
    remaining_actors_list = actor_manager.all()
    print("Remaining actors:", remaining_actors_list)
