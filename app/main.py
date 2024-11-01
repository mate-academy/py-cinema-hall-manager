from managers import ActorManager

if __name__ == "__main__":
    actor_manager = ActorManager()
    actor_manager.create(first_name="Емма", last_name="Ватсон")
    actor_manager.create(first_name="Деніел", last_name="Редкліфф")
    print(actor_manager.all())
    actor_manager.update(actor_id=2, first_name="Деніел", last_name="Редкліфф")
    print(actor_manager.all())
    actor_manager.delete(actor_id=1)
    print(actor_manager.all())
