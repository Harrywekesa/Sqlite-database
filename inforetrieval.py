import sqlite3

#select first and last names of people over the age of 30
with sqlite3.connect("insert_many.db") as conn:
    c = conn.cursor()
    c.execute("SELECT First_name, Last_name FROM people WHERE Age > 20")
    for row in c.fetchall():
        print(row)
    