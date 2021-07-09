import sqlite3

#get personal data from the user
First_name = input("Enter your first name: ")
Last_name = input("Enter your last name: ")
Age = int(input("Enter your age:"))

#Execute insert statement for supplied user data
with sqlite3.connect("uinput.db") as conn:
    c = conn.cursor()
    c.execute("CREATE TABLE people(First_name TEXT, Last_name TEXT, Age INT)")
    line = "INSERT INTO people VALUES('" + First_name + "', '" + Last_name + "', " + str(Age) + ")"
    c.execute(line)
    
#NOTE it is not safe to use '' "" to denote srings because they are easily breakable instead use placeholders