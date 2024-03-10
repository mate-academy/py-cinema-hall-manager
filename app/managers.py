import sqlite3


class ActorManager:
    def __init__(self) -> None:
        self.connect = sqlite3.connect("../cinema.sqlite")

    def create(self, first_name: str, last_name: str) -> None:
        sql = "Insert Into actors (first_name,last_name) VALUES (?,?)"
        self.connect.execute(sql, (first_name, last_name))
        self.connect.commit()

    def all(self) -> None:
        actors = self.connect.execute("Select * From actors")
        print([actor for actor in actors])
        return actors

    def update(self, id: int, first_name: str, last_name: str) -> None:
        sql = "Update actors Set first_name = ?, last_name = ? Where id = ?"
        self.connect.execute(sql, (first_name, last_name, id))
        # self.connect.commit()

    def delete(self, id: int) -> None:
        sql = "Delete From actors Where id = ?"
        self.connect.execute(sql, (id,))
        self.connect.commit()
