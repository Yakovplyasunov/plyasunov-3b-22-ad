import sqlite3


DATABASE_NAME = "books"
FIELDS = {"title":"TEXT",
          "author":"TEXT",
          "year": "INTEGER"}
SELECTED_FIELD = ""
VALUES = [('The Hunger Games', 'Suzanne Collins', 2008),
          ('Harry Potter and the Sorcerer' , 'J.K. Rowling', 1997),
          ('The Da Vinci Code', 'Dan Brown', 2003),
          ('The Girl with the Dragon Tattoo', 'Stieg Larsson', 2005),
          ('The Help', 'Kathryn Stockett', 2009),
]
CONDITION = "year > 2000"


conn = sqlite3.connect(f"{DATABASE_NAME}_database.db")

cursor = conn.cursor()
cursor.execute(f'''
CREATE TABLE IF NOT EXISTS {DATABASE_NAME}
(id INTEGER PRIMARY KEY, {', '.join([f"{key} {value}" for key, value in FIELDS.items()])})
''')
cursor.executemany(f"INSERT INTO {DATABASE_NAME} ({', '.join(FIELDS.keys())}) VALUES ({', '.join(['?'] * len(FIELDS))})", VALUES)
conn.commit()

cursor.execute(f"SELECT {SELECTED_FIELD or '*'} FROM {DATABASE_NAME} {f'WHERE {CONDITION}' if CONDITION else ''}")
columns = [*zip(*cursor.description)][0]
result = [columns] + cursor.fetchall()
lengths = []

for indx, column in enumerate(columns):
    cursor.execute(f"SELECT max(length({column})) FROM {DATABASE_NAME} {f'WHERE {CONDITION}' if CONDITION else ''}")
    lengths.append(max(cursor.fetchone()[0], len(column)))

[print('   '.join([f"{row[i]:^{lengths[i]}}" for i in range(len(columns))])) for row in result]

conn.close()
