import pytest
from managers import ActorManager
from models import Actor


@pytest.fixture
def setup_database() -> None:
    manager = ActorManager()
    manager.create("Emma", "Watson")
    yield manager
    manager._connection.execute("DELETE FROM actors")
    manager._connection.commit()


def test_create_actor(setup_database: ActorManager) -> None:
    manager = setup_database
    manager.create("Daniel", "Radcliffe")
    actors = manager.all()
    assert len(actors) == 2
    assert actors[1] == Actor(id=2, first_name="Daniel", last_name="Radcliffe")


def test_update_actor(setup_database: ActorManager) -> None:
    manager = setup_database
    manager.update(1, "Emma", "Watson-Updated")
    actor = manager.all()[0]
    assert actor.first_name == "Emma"
    assert actor.last_name == "Watson-Updated"


def test_delete_actor(setup_database: ActorManager) -> None:
    manager = setup_database
    manager.delete(1)
    actors = manager.all()
    assert len(actors) == 0
