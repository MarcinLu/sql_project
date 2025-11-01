import pyodbc

try:
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=TestDB;'
        'Trusted_Connection=yes;'
    )
    print("✅ Połączenie z bazą TestDB działa!")
except Exception as e:
    print("❌ Błąd połączenia:")
    print(e)