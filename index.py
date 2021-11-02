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
    print("Uspješna registracija")
