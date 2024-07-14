from managers import ActorManager


def main():
    manager = ActorManager()

    # Створення нових акторів
    manager.create('Leonardo', 'DiCaprio')
    manager.create('Morgan', 'Freeman')

    # Отримання всіх акторів
    actors = manager.all()
    print("Actors in database:")
    for actor in actors:
        print(actor)

    # Оновлення інформації про актора
    manager.update(1, new_first_name='Leonard', new_last_name='DiCaprio')

    # Видалення актора
    manager.delete(2)

    # Отримання всіх акторів після оновлення та видалення
    actors = manager.all()
    print("Actors in database after update and delete:")
    for actor in actors:
        print(actor)


if __name__ == '__main__':
    main()
