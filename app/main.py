# from models import Actor
# from managers import ActorManager
#
# if __name__ == "__main__":
#     Actor.objects = ActorManager()
#
#     Actor.objects.create(first_name="Emma", last_name="Watson")
#     Actor.objects.create(first_name="Daniel", last_name="Radclife")
#     print(Actor.objects.all())
#     Actor.objects.update(2, "Daniel", "Radcliffe")
#     print(Actor.objects.all())
#     Actor.objects.delete(1)
#     print(Actor.objects.all())


import sqlite3

connection = sqlite3.connect('c:/Users/ya/projects/py-actor-manager/app/cinema.sqlite')
cursor = connection.cursor()

# Создание таблицы actors
cursor.execute('''CREATE TABLE IF NOT EXISTS actors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
)''')

connection.commit()
connection.close()
