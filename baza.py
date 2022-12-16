import sqlite3

conn = sqlite3.connect('dane.sqlite')

c = conn.cursor()

# c.execute('''
#             CREATE TABLE transakcje
#             (data TEXT, id INTEGER, cena REAL)
# ''')

c.execute('''
            INSERT INTO transakcje VALUES
            ('2022-12-16', 11, 17.50)
''')

c.execute('''
            INSERT INTO transakcje VALUES
            ('2022-12-11', 10, 217.50)
''')

c.execute('''
            INSERT INTO transakcje VALUES
            ('2022-12-12', 14, 3217.50)
''')
lista2 = ('2022-11-30', 16, 1233.44)
c.execute(f'''
        INSERT INTO transakcje VALUES
        {lista2}
''')
lista = []

for row in c.execute('SELECT * FROM transakcje ORDER BY cena DESC'):
    print(row)
    lista.append(row)

conn.commit()
conn.close()
