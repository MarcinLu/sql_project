import pyodbc

try:
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=localhost\\SQLEXPRESS;'
        'DATABASE=TestDB;'
        'Trusted_Connection=yes;'
    )
    print("✅ Połączenie z bazą działa!")
except Exception as e:
    print("❌ Błąd połączenia:", e)
