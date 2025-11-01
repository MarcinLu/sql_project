import pyodbc

# nazwa serwera i bazy do testu
SERVER = 'localhost'  # domyślna instancja
DATABASE = 'TestDB'

drivers = pyodbc.drivers()
print("Dostępne sterowniki ODBC:")
for d in drivers:
    print(f"- {d}")

print("\nTestujemy połączenia z TestDB...\n")

for driver in drivers:
    try:
        print(f"Próba połączenia przy użyciu sterownika: {driver}")
        conn = pyodbc.connect(
            f'DRIVER={{{driver}}};'
            f'SERVER={SERVER};'
            f'DATABASE={DATABASE};'
            f'Trusted_Connection=yes;'
            f'Encrypt=no'  # dla lokalnego połączenia
        )
        print(f"✅ Połączenie OK z użyciem sterownika: {driver}\n")
        conn.close()
    except Exception as e:
        print(f"❌ Błąd połączenia z użyciem sterownika {driver}: {e}\n")
