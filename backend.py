import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title text,author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def drop():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DROP TABLE book")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()
def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? AND author = ? AND year = ? AND isbn = ?",(title,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ?,author =?,year = ?,isbn = ? WHERE id = ?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()


drop()
connect()
insert("SHEESHU","CHUNI",2021,9030765075)
insert("MONKEY","DOGGY",2021,9030765075)
insert("CHEECHU","PIGGY",2021,9030765075)
insert("SHEECHU","SLEEPY",2021,9030765075)
insert("POTTI","SLEEPY",2021,9030765075)

