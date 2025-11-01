import pyodbc

conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=localhost;'
    'DATABASE=TestDB;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()
cursor.execute('SELECT * FROM Products')
rows = cursor.fetchall()

for row in rows:
    print(row.ProductID, row.ProductName, row.Category, row.UnitPrice)

cursor.close()
conn.close()