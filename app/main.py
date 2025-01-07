from managers import ActorManager

if __name__ == "__main__":
    with ActorManager() as actor_manager:
        actor_manager.create(first_name="Emma", last_name="Watson")
        actor_manager.create(first_name="Daniel", last_name="Radclife")
        print(actor_manager.all())

        actor_manager.update(2, "Daniel", "Radcliffe")
        print(actor_manager.all())
        actor_manager.delete(1)
        print(actor_manager.all())

        # actor_manager.delete_all()
