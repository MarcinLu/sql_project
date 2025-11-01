import pyodbc

conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=localhost;'      # domyślna instancja
    'DATABASE=TestDB;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()
cursor.execute('SELECT TOP 5 * FROM Products')
for row in cursor:
    print(row)
cursor.close()
conn.close()
