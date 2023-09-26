from unittest import TestCase
from unittest import mock
from unittest.mock import Mock

from app.controller import ActorsController
from app.models import Actor


class TestActorsTable(TestCase):
    def setUp(self) -> None:
        self.table = ActorsController().table()
        self.test_actor = ("name", "surname")
        self.test_actor_id = 0

    @mock.patch("app.managers.ActorManager.create")
    def test_create(self, mocked_create: Mock) -> None:
        self.table.create(*self.test_actor)
        mocked_create.assert_called_once_with(*self.test_actor)

    def test_all(self) -> None:
        bool_ls = [
            True if isinstance(value, Actor)
            else False
            for value in self.table.all()
        ]
        assert all(bool_ls) is True

    @mock.patch("app.managers.ActorManager.update")
    def test_update(self, mocked_update: Mock) -> None:
        data = self.test_actor_id, *self.test_actor
        self.table.update(*data)
        mocked_update.assert_called_once_with(*data)

    @mock.patch("app.managers.ActorManager.delete")
    def test_delete(self, mocked_delete: Mock) -> None:
        self.table.delete(self.test_actor_id)
        mocked_delete.assert_called_once_with(self.test_actor_id)
