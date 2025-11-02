import pyodbc

# Parametry połączenia
SERVER = 'localhost'
DATABASE = 'TestDB'
DRIVER = 'ODBC Driver 17 for SQL Server'

# Połączenie z bazą danych
conn = pyodbc.connect(
    f'DRIVER={{{DRIVER}}};'
    f'SERVER={SERVER};'
    f'DATABASE={DATABASE};'
    f'Trusted_Connection=yes;'
    f'Encrypt=no'
)
cursor = conn.cursor()

print("✅ Połączono z bazą danych TestDB!")

# zapytanie
cursor.execute("SELECT TOP 5 * FROM Users")
rows = cursor.fetchall()

print("\n👥 Lista użytkowników:")
for row in rows:
    print(row)

cursor.close()
conn.close()
print("\n🔒 Połączenie zamknięte.")