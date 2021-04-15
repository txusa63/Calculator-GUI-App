import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS tape_data(id INTEGER PRIMARY KEY, operations text, result text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT operations, result FROM tape_data")
        rows = self.cur.fetchall()
        return rows

    def insert(self, operations, result):
        self.cur.execute("INSERT INTO tape_data VALUES (NULL, ?, ?)", (operations, result))
        self.conn.commit()

    def remove(self):
        self.cur.execute("DELETE FROM tape_data")
        self.conn.commit()

    def __del__(self):
        self.conn.close()
