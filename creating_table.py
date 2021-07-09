#Importing sqlit3 library
import sqlite3

# Creating a new database if the database doesn't already exist
conn = sqlite3.connect("new.db") 

#If you want to create  a table in the RAM
# conn = sqlite3.connect(':memory:')

# Getting a cursor object used to execute sql commands/query
cursor = conn.cursor()

#Create a table
cursor.execute("""CREATE TABLE population(city TEXT, county TEXT, population INTEGER)""")


#Inserting data to the table population
cursor.execute("""INSERT INTO population VALUES('Nairobi', 'Nairobi', 2000000)""")
conn.commit()

#close the database connection
conn.close()


#Deleting a table
#conn.execute("Drop TABLE IF EXISTS population") #Here we check if the table already exists before dropping


#It is recommended to use the """with""" keyword  when working with the database connection to simplify your
#code .ie.
#with sqlite3.connect("test_db.db") as connection:
    #perform operations here