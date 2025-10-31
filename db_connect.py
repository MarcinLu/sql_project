import pyodbc

# Połączenie z lokalnym SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=TestDB;'
    'Trusted_Connection=yes;'
    'TrustServerCertificate=yes;'
)

cursor = conn.cursor()

# Przykładowe zapytanie
cursor.execute("SELECT name FROM sys.databases;")

print("Dostępne bazy danych:")
for row in cursor:
    print("-", row[0])

cursor.close()
conn.close()