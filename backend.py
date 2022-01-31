import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (book_id INTEGER PRIMARY KEY, title TEXT,author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()
    
def insert(t,a,y,i):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book (title,author,year,isbn) VALUES (?,?,?,?)",(t,a,y,i))
    conn.commit()
    conn.close()
    
def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    
    return rows

def search(t="",a="",y="",i=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(t,a,y,i))
    rows = cur.fetchall()
    conn.close()
    
    return rows

def update(bi,t,a,y,i):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE book_id=?",(t,a,y,i,bi))
    conn.commit()
    conn.close()
    
def delete(i):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE book_id=?",(i,))
    conn.commit()
    conn.close()

connect()
