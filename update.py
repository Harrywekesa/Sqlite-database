import sqlite3

#Updating the contents of a row
with sqlite3.connect("script.db") as conn:
    c = conn.cursor()
    c.execute("UPDATE people SET Age = ? WHERE First_name = ? AND Last_name = ?", (45, 'Wafula', 'Brian'))