#Importing sqlit3 library
import sqlite3

# Creating a new database if the database doesn't already exist
conn = sqlite3.connect("new.db") 

# Getting a cursor object used to execute sql commands/query
cursor = conn.cursor()

#Create a table
cursor.execute("""CREATE TABLE population(city TEXT, state TEXT, population INTEGER)""")

#close the database connection
conn.close()