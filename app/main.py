from managers import ActorManager

if __name__ == "__main__":
    actor_manager = ActorManager()

    actor_manager.create(first_name="Emma", last_name="Watson")
    actor_manager.create(first_name="Daniel", last_name="Radcliffe")

    print(actor_manager.all())

    actor_manager.update(
        id_to_update=2,
        new_first_name="Dan",
        new_last_name="Radcliffe"
    )

    print(actor_manager.all())

    actor_manager.delete(id_to_delete=1)

    print(actor_manager.all())
