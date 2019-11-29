import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, price integer, year integer)")
    conn.commit()
    conn.close()

def insert(title="",author="",price="",year=""):
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,price,year))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("SELECT * FROM book")
    rows=curr.fetchall()
    conn.close()    
    return rows

def search(title="",author="",price="",year=""):
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("SELECT * FROM book WHERE title=? OR author=? OR price=? OR year=?",(title,author,price,year))
    rows=curr.fetchall()
    conn.close()      
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()   

def update(id,title,author,price,year):
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("UPDATE book SET title=?,author=?,price=?,year=? WHERE id=?",(title,author,price,year,id))
    conn.commit()
    conn.close()

connect()