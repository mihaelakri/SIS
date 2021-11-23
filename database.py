import sqlite3
con = sqlite3.connect('db.db')

cur = con.cursor()

cur.execute('''CREATE TABLE user
                (ID integer primary key, ime text, email text, password text, kontakt text, created_at text, brPrijava integer DEFAULT 0)''')

con.commit()
con.close()

