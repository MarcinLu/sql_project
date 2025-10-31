cursor.execute("""
INSERT INTO Users (Name, Email)
VALUES (?, ?)
""", ("Anna Nowak", "anna@nowak.pl"))
conn.commit()