# Part 1 - Making and populating a Database
# Consider the following data:

# s    x	y
# 'g'	3	9
# 'v'	5	7
# 'f'	8	7
# Using the standard sqlite3 module:
import sqlite3


# Open a connection to a new (blank) database file
sqlite_conn = sqlite3.connect('demo_data.sqlite3')

# Make a cursor,
sqlite_cursor = sqlite_conn.cursor()

# and execute an appropriate CREATE TABLE statement to accept the above
# data (name the table demo)

# BEFORE CREATING THE TABLE, DROP IT IF EXISTS
# Exercise complete.
# sqlite_cursor.execute('DROP TABLE IF EXISTS demo')

create_table_sql = """CREATE TABLE  demo(
   id NUMBER PRIMARY KEY,
   s TEXT,
   x NUMBER,
   y NUMBER
);"""

sqlite_cursor.execute(create_table_sql)

# Write and execute appropriate INSERT INTO statements to add the data
# (as shown above) to the database

# def quick_insert(s, x, y):
#     sqlite_cursor.execute("""INSERT INTO demo (s, x, y)
# VALUES('""" + s + "', " + str(x) + ", " + str(y) + ");")
#     sqlite_conn.commit()

# def print_insert(s, x, y):
#     print("""INSERT INTO demo (s, x, y)
# VALUES('""" + s + "', " + str(x) + ", " + str(y) + ");")


sqlite_cursor.execute("""INSERT INTO demo (s, x, y)
VALUES('g', 3, 9);""")
# Make sure to commit() so your data is saved!
# The file size should be non-zero.
sqlite_conn.commit()

sqlite_cursor.execute("""INSERT INTO demo (s, x, y)
VALUES('v', 5, 7);""")
# Make sure to commit() so your data is saved!
# The file size should be non-zero.
sqlite_conn.commit()

sqlite_cursor.execute("""INSERT INTO demo (s, x, y)
VALUES('f', 8, 7);""")
# Make sure to commit() so your data is saved!
# The file size should be non-zero.
sqlite_conn.commit()


# INSERT INTO demo (s, x, y)
# print_insert('g', 3, 9)
# print_insert('v', 5, 7)
# print_insert( 'f', 8, 7)

# INSERT INTO demo (s, x, y)
# quick_insert('g', 3, 9)
# quick_insert('v', 5, 7)
# quick_insert( 'f', 8, 7)

# Then write the following queries (also with sqlite3) to test:

# Count how many rows you have - it should be 3!
result = sqlite_cursor.execute("""SELECT COUNT (*) FROM demo""").fetchall()
print(result)

# result = [(3,)] -- good


# How many rows are there where both x and y are at least 5?
sql = """SELECT COUNT (*) FROM demo
WHERE x >= 5 AND Y >= 5"""

result = sqlite_cursor.execute(sql).fetchall()
print(result)
# result = [(2,)] - correct


# How many unique values of y are there (hint -
# COUNT() can accept a keyword DISTINCT)?

sql = """SELECT COUNT(DISTINCT y) FROM demo;"""
result = sqlite_cursor.execute(sql).fetchall()
print(result)
# result = [(2,)] - correct

# print("here")

# Your code (to reproduce all above steps) should be saved in demo_data.py
# and added to the repository along with the generated SQLite database.
