import sqlite3
from hashlib import blake2b
from datetime import date

con = sqlite3.connect('db.db')


def register_user(ime, email, lozinka, kontakt, datum):
    cur = con.cursor()
    transbyte = str.encode(lozinka)
    h = blake2b()
    h.update(transbyte)
    lozinka = h.hexdigest()
    cur.execute("INSERT INTO user (ime, email, password, kontakt, created_at) values(?, ?, ?, ?, ?);", (ime, email, lozinka, kontakt, datum))
    print("Prijava uspješna!")
    
    con.commit()
    con.close()
    
    
datum = date.today()

print("Dobrodošli u Unidu sustav!")
print("Za prijavu upišite broj 1, za registraciju broj 2")

broj = int(input("Unesite broj: "))
while broj != 1 and broj != 2:
    broj = int(input("Unesite broj: "))


if broj == 1:
    email = input("Unesi email: ")
    while email == "":
        email = input("Unesi email: ")
    lozinka = input("Unesi lozinku: ")
    while lozinka == "":
        lozinka = input("Unesi lozinku: ")
    print("Uspješna prijava")
if broj == 2:
    ime = input("Unesi ime: ")
    while ime == "":
        ime = input("Unesi ime: ")
    email = input("Unesi email: ")
    while email == "":
        email = input("Unesi email: ")
    lozinka = input("Unesi lozinku: ")
    while lozinka == "":
        lozinka = input("Unesi lozinku: ")
    kontakt = input("Unesi broj mobitela: ")
    while kontakt == "":
        kontakt = input("Unesi broj mobitela: ")
    register_user(ime, email, lozinka, kontakt, datum)
    
    
    
