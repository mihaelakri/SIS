import sqlite3
con = sqlite3.connect('db.db')

cur = con.cursor()

cur.execute('''CREATE TABLE user
                (ID int primary key, ime text, email text, password text, kontakt text, created_at text)''')

con.commit()
con.close()

