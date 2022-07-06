import sqlite3

# Create a database in RAM
db = sqlite3.connect(':memory:')

# Get a cursor object
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE count_demos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    val INT
    );''')

# Insert users
cursor.execute('''INSERT INTO count_demos(val) VALUES (-1),(1),(1),(3),(NULL),(3),(4),(6),(NULL),(8),(9),(10)''');
#Select user

cursor.execute('''SELECT DISTINCT val FROM count_demos''');
#retrieve the first row
user1 = cursor.fetchall()
#Print the first column retrieved(user's name)
print(user1)

#Commit changes into database
db.commit()
#Close database
db.close()
