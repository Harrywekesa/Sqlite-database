import sqlite3

values = (("Jean-Baptiste Zorg", "Human", 122), ("Korben Dallas", "Meat Popssicle", 100), ("Ak'not", "Mangalore", -5))

with sqlite3.connect(":memory:&db") as conn:
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS Roster")
    c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO Roster VALUES(?, ?, ?)", values) #This inserts all the data in the list to the database
    c.execute("UPDATE Roster SET Species = ? WHERE Name = ? AND IQ = ?", ("Human", "Korben Dallas", 100))   
    c.execute("SELECT Name, IQ FROM Roster WHERE Species is 'Human'")
    for row in c.fetchall():
        print(row)
