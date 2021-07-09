import sqlite3

people_values = (("Harrison", "Wekesa", 23), ("Yvonne", "Nekesa", 15), ("Mercy", "Nasimiyu", 14),\
    ("Sout","Nam", 45), ("Sin", "wer", 97), ("Sila", "Simiyu", 34), ("Evans", "Kipkorir", 24))

with sqlite3.connect("insert_many.db") as conn:
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS people")
    c.execute("CREATE TABLE people(First_name TEXT, Last_name TEXT, Age INT)")
    c.executemany("INSERT INTO people VALUES(?, ?, ?)", people_values) #This inserts all the data in the list to the database
        
    
