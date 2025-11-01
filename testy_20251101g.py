import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'  # używamy nowego sterownika
    'SERVER=localhost;'                         # domyślna instancja
    'DATABASE=TestDB;'
    'Trusted_Connection=yes;'
    'Encrypt=no'                                # konieczne dla lokalnego połączenia
)

cursor = conn.cursor()
cursor.execute('SELECT TOP 5 * FROM Products')
for row in cursor:
    print(row)
cursor.close()
conn.close()
