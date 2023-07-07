import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students
(id INTEGER PRIMARY KEY, name TEXT, age INTEGER, average_score REAL)''')

students_data = [('Yakov', 18, 4.2),
                 ('Oleg', 19, 4.9),
                 ('Sveta', 18, 3.8)]

cursor.executemany("INSERT INTO students (name, age, average_score) VALUES (?, ?, ?)", students_data)

conn.commit()

cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

for row in rows:
    print(f'Name: {row[1]}, Age: {row[2]}, Average Score: {row[3]}')

conn.close()
