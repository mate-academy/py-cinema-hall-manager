import os.path
from models import Actor
from managers import ActorManager
from managers import db_path

if __name__ == "__main__":
    Actor = ActorManager()

    # Actor.create(first_name_="Emma", last_name_="Watson")
    # Actor.create(first_name_="Daniel", last_name_="Radclife")
    # Actor.objects.update(2, "Daniel", "Radcliffe")
    # Actor.objects.delete(1)
    # print(Actor.objects.all())

    print(db_path)


