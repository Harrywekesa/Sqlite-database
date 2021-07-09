import sqlite3

with sqlite3.connect("script.db") as conn:
    c = conn.cursor()
    c.executescript(""" DROP TABLE IF EXISTS people;
                    CREATE TABLE people(First_name TEXT, Last_name TEXT, Age INT);
                    INSERT INTO people VALUES ('Harrison', 'Wekesa',22);
                    """)

#Executescript()/ executemany() is used when running more than one line of SQL code at a time