# -*- coding: utf-8 -*-
# MySQL Workbench Python script
# <description>
# Written in MySQL Workbench 6.3.8

import grt
#import mforms
"""
Skip to content
Sign up
Kalpesh14m 
Python-For-Everybody-Answers
Public

Code
Issues
Pull requests 1
Actions
Projects
Wiki
Security

More
Python-For-Everybody-Answers/4-Using-Database-With_Python/Assignment/Week 2 Assignment 2.1 Our First Database.py /
@Kalpesh14m
Kalpesh14m All Python For everybody Quiz and Assignment with Answers
Latest commit 4cd08bc on 26 Jun 2018
History
1 contributo
62 lines (46 sloc) 1.79 KB"""
"""
To get credit for this assignment, perform the instructions below and enter the code you get here:
(Hint: starts with 467)
Instructions
create a SQLITE database or use an existing database and create a table in the database called "Ages":
CREATE TABLE Ages (
  name VARCHAR(128),
  age INTEGER
)
Then make sure the table is empty by deleting any rows that you previously inserted, and insert these rows and only these rows with the following commands:
DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Mara', 28);
INSERT INTO Ages (name, age) VALUES ('Otto', 33);
INSERT INTO Ages (name, age) VALUES ('Fyn', 31);
INSERT INTO Ages (name, age) VALUES ('Neshawn', 17);
Once the inserts are done, run the following SQL command:
SELECT hex(name || age) AS X FROM Ages ORDER BY X
Find the first row in the resulting record set and enter the long string that looks like 53656C696E613333.
Answer ==> The first row in the resulting record set : 46796E3331
"""
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
