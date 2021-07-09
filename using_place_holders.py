import sqlite3

#Get personal data from the user aand insert it into a tuple
First_name = input("Enter your first name: ")
Last_name = input("Enter your last name: ")
Age = input("Enter your age: ")
personal_data = (First_name, Last_name, Age)

#Execute insert statement for supplied personal data
with sqlite3.connect("place_holder.db") as conn:
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS people")
    c.execute("CREATE TABLE people(First_name TEXT, Last_name TEXT, Age INT)")
    c.execute("INSERT INTO people VALUES(?, ?, ?)", personal_data)


