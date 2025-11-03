import pyodbc
import pandas as pd
import matplotlib.pyplot as plt

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

# --- Pobranie danych z tabeli Orders ---
query = """
SELECT Status, COUNT(*) AS CountStatus
FROM dbo.Orders
GROUP BY Status
ORDER BY Status
"""
df = pd.read_sql(query, conn)

# Zamknięcie połączenia
conn.close()

# --- Wizualizacja danych ---
plt.figure(figsize=(8, 5))
plt.bar(df['Status'], df['CountStatus'], color=['green', 'orange', 'red'])
plt.title('Liczba zamówień wg statusu', fontsize=14)
plt.xlabel('Status zamówienia')
plt.ylabel('Liczba zamówień')
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Dodanie etykiet wartości nad słupkami
for i, val in enumerate(df['CountStatus']):
    plt.text(i, val + 0.1, str(val), ha='center', va='bottom', fontsize=10)

# Wyświetlenie wykresu
plt.tight_layout()
plt.show()
