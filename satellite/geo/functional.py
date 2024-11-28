import duckdb

from satellite.geo.constants import ADM_DB


class SessionContextManager:
    def __init__(self, db: str):
        self.conn = duckdb.connect(db, read_only=True)

    def __enter__(self):
        return self.conn.begin()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()


def session(engine=ADM_DB) -> SessionContextManager:
    return SessionContextManager(engine)
