import sqlite3

# Create Database class
class Database:
    # Initialize a database named 'todo'
    def __init__(self):
        self.conn = sqlite3.connect("todo.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS todo(id INTEGER PRIMARY KEY, task text, date integer, time integer, priority text)")
        self.conn.commit()

    # Function to insert into database the necessary elements for the task manager app
    def insert(self,task, date, time, priority):
        self.cur.execute("INSERT INTO todo VALUES (NULL,?,?,?,?)", (task, date, time, priority))
        self.conn.commit()

    # Function to view the database
    def view(self):
        self.cur.execute("SELECT * FROM todo")
        rows = self.cur.fetchall()
        return rows
    
    # Function to search a specfic row in the database
    def search(self,task="", date="", time="", priority=""):
        self.cur.execute("SELECT * FROM todo WHERE task=? OR date=? OR time=? OR priority=?", (task, date, time, priority))
        rows = self.cur.fetchall()
        return rows

    # Function to delete a row in the database
    def delete(self,id):
        self.cur.execute("DELETE FROM todo WHERE id=?", (id,))
        self.conn.commit()

    # Function to update a row in the database
    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE todo SET task=?, date=?, time=?, priority=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()

    # Function to close the connection to the database
    def __del__(self):
        self.conn.close()
