import sqlite3

import pytest

from app.managers import ActorManager
from app.models import Actor


class TestActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def delete_all(self) -> None:
        self._connection.execute("DELETE FROM actors")
        self._connection.commit()

    def create(self, first_name: str, last_name: str = None) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?)", (first_name, last_name))
        self._connection.commit()

    def all(self) -> list[Actor]:
        self.actors_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in self.actors_cursor]


@pytest.fixture
def test_actor_manager() -> TestActorManager:
    yield TestActorManager()
    TestActorManager().delete_all()


@pytest.fixture
def actor_manager() -> ActorManager:
    return ActorManager()


def test_method_should_create(
        actor_manager: ActorManager,
        test_actor_manager: TestActorManager
) -> None:
    actor_manager.create("John", "Smith")
    assert test_actor_manager.all() == [
        Actor(id=1, first_name="John", last_name="Smith")
    ]


def test_should_update_values(
        actor_manager: ActorManager,
        test_actor_manager: TestActorManager
) -> None:
    test_actor_manager.create("John", "Smith")
    actor_manager.update(1, "Ivan", "Sydorenko")
    assert test_actor_manager.all() == [
        Actor(id=1, first_name="Ivan", last_name="Sydorenko")
    ]


def test_should_delete_values(
        actor_manager: ActorManager,
        test_actor_manager: TestActorManager
) -> None:
    test_actor_manager.create("John", "Smith")
    actor_manager.delete(1)
    assert test_actor_manager.all() == []


def test_should_read_a_value(
        actor_manager: ActorManager,
        test_actor_manager: TestActorManager
) -> None:
    test_actor_manager.create("John", "Smith")
    assert actor_manager.all() == [
        Actor(id=1, first_name="John", last_name="Smith")
    ]
