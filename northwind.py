import sqlite3

# Using sqlite3, connect to the given
# northwind_small.sqlite3 database.

sqlite_conn = sqlite3.connect('northwind_small.sqlite3')

# Make a cursor,
sqlite_cursor = sqlite_conn.cursor()

# What are the ten most expensive items
# (per unit price) in the database?

sql = """select ProductName, UnitPrice FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
"""
result = sqlite_cursor.execute(sql).fetchall()
print("Ten most expensive items (unit price):")
for r in result:
    print(r[0])

# Côte de Blaye
# Thüringer Rostbratwurst
# Mishi Kobe Niku
# Sir Rodney's Marmalade
# Carnarvon Tigers
# Raclette Courdavault
# Manjimup Dried Apples
# Tarte au sucre
# Ipoh Coffee
# Rössle Sauerkraut

# What is the average age of an employee at the time of their hiring? (Hint: a
# lot of arithmetic works with dates.)

sql3 = """SELECT ROUND( (AVG (julianday(HireDate) - julianday(BirthDate)) /365), 2)
FROM Employee"""

r = sqlite_cursor.execute(sql3).fetchall()

print()
print("The average age of an employee at the time of their hiring is")
print(f"{r[0][0]} years.")
#print(f"{round(r[0][0]/365,2)} years")


#What are the ten most expensive items (per unit price) in the database *and*
#  their suppliers?

sql4 = """select ProductName, UnitPrice, CompanyName FROM Product
INNER JOIN Supplier
ORDER BY UnitPrice DESC
LIMIT 10"""

results = sqlite_cursor.execute(sql4).fetchall()


print("""The ten most expensive items (per unit price) in the database *and* their suppliers are:""")
for r in results:
    print(f"Product: {r[2]}, Supplier: {r[0]}")


sql5 = """select CategoryName, COUNT (Product.ID), Category.Id FROM Product
inner join Category
GROUP BY Category.Id
LIMIT 1
"""
print()
print("The largest category (by number of unique products in it) is:")
r = sqlite_cursor.execute(sql5).fetchall()
print(r[0][0])



