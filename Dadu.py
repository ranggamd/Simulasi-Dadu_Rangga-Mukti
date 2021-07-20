import random

putaran= {}

def putardadu(min, max):
    while True:
        print("Memutar Dadu.....")
        angka = random.randint(min, max)
        if angka in putaran:
            putaran[angka] +=1
        else:
            putaran[angka] =1
        print(f"Kamu Dapat Angka : {angka}")
        choice = input("Apakah anda ingin memutar dadu lagi (y/n)?")
        if choice.lower() == 'n' or choice.lower() == 'N':
            for angka in putaran:
                print("Angka", str(angka), "di dapat sebanyak", str(putaran[angka]), "kali.")

        if choice.lower() == 'y' or choice.lower() == 'Y':
            choice=False

        else:
            break

putardadu(1,6)
