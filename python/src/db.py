import sqlite3
DATABASE_NAME = "test.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """
        CREATE TABLE IF NOT EXISTS activity (
            date TEXT not null,
            name TEXT not null,
            duration integet not null,
            distance integet not null
        )
        """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
