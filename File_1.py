# -*- coding: utf-8 -*-
# MySQL Workbench Python script
# <description>
# Written in MySQL Workbench 6.3.8

import grt
#import mforms
import sqlite3

# Create a database in RAM
db = sqlite3.connect(':memory:')

# Get a cursor object
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)''')


cursor.execute('''DELETE FROM Ages''')

# Insert users
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Mara', 28)''')
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Otto', 33)''')
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Fyn', 31)''')
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Neshawn', 17)''')

#Select user
cursor.execute('''SELECT hex(name || age) AS X FROM Ages ORDER BY X''')

#retrieve the first row
user1 = cursor.fetchmany(3)
#Print the first column retrieved(user's name)

print(user1)

#Commit changes into database
db.commit()
#Close database
db.close()