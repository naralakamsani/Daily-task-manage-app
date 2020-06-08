import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("todo.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS todo(id INTEGER PRIMARY KEY, task text, date integer, time integer, priority text)")
        self.conn.commit()

    def insert(self,task, date, time, priority):
        self.cur.execute("INSERT INTO todo VALUES (NULL,?,?,?,?)", (task, date, time, priority))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM todo")
        rows = self.cur.fetchall()
        return rows

    def search(self,task="", date="", time="", priority=""):
        self.cur.execute("SELECT * FROM todo WHERE task=? OR date=? OR time=? OR priority=?", (task, date, time, priority))
        rows = self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM todo WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE todo SET task=?, date=?, time=?, priority=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
