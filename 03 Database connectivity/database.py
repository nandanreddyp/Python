import sqlite3

conn = sqlite3.connect('db.sqlite')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE Ages (
    name VARCHAR(128),
    age INTEGER
)
''')
conn.commit()

cursor.execute('DELETE FROM Ages')
cursor.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Bronagh', 22))
cursor.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Ghalya', 19))
cursor.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Archibald', 25))
cursor.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Jorjia', 29))
cursor.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Verity', 37))
cursor.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Kern', 18))
conn.commit()

cursor.execute('''
SELECT hex(name || age) AS X FROM Ages ORDER BY X
''')
rows = cursor.fetchall()

print(rows)

conn.close()