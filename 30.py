from contextlib import contextmanager


@contextmanager
def db_connection(conn_str: str):
    try:
        print("Connected")
        yield 1
    finally:
        print("Closed")


with db_connection("test") as conn:
    print("HElo")
    raise Exception("something went wrong")
