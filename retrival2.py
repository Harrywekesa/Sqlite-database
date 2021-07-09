import sqlite3

#select first and last names of people over the age of 30
with sqlite3.connect("insert_many.db") as conn:
    c = conn.cursor()
    c.execute("SELECT First_name, Last_name FROM people WHERE Age > 20")
    while True:
        row = c.fetchone() #This loops over the results one row at a time
        if row is None:
            break
        print(row)
    