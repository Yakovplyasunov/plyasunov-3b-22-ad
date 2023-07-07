import sqlite3


DATABASE_NAME = "employees"
FIELDS = {"name":"TEXT",
          "position":"TEXT",
          "salary": "REAL"}
SELECTED_FIELD = "name"
VALUES = [ ('Christopher', 'Director', 1500000),
          ('Emma', 'Actress', 1000000),
          ('Oliver', 'Producer', 900000),
          ('Sophia', 'Screenwriter', 800000),
          ('Alexander', 'Cinematographer', 500000),
]
CONDITION = "position = 'Producer'"


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
result = [columns] + cursor.fetchall() if len(columns) > 1 else cursor.fetchall()
lengths = []

for indx, column in enumerate(columns):
    cursor.execute(f"SELECT max(length({column})) FROM {DATABASE_NAME} {f'WHERE {CONDITION}' if CONDITION else ''}")
    lengths.append(max(cursor.fetchone()[0], len(column)))

[print('   '.join([f"{row[i]:^{lengths[i]}}" for i in range(len(columns))])) for row in result]

conn.close()
