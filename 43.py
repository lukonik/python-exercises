from __future__ import annotations


class Database:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Database, cls).__new__(cls)

        return cls.__instance


db1 = Database()
db2 = Database()
print(db1 is db2)
