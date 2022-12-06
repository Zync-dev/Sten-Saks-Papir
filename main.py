import time
import random
import webbrowser

while True:
    AIChoices = ["Sten", "Saks", "Papir"]

    choose = input("Hvad vælger du?\n(1) Sten\n(2) Saks\n(3) Papir\nSkriv her: ")

    if choose == "1":
        print("\nDu valgte Sten!")
    elif choose == "2":
        print("\nDu valgte Saks!")
    elif choose == "3":
        print("\nDu valgte Papir")

    time.sleep(2)

    randomint = random.randint(0, 2)
    print("\nDin modstander valgte " + str(AIChoices[randomint]) + "\n")

    time.sleep(2)

    if choose == "1" and randomint == 2:
        print("Du tabte desværre!")
    elif choose == "1" and randomint == 1:
        print("Tillykke! Du vandt.")
    elif choose == "1" and randomint == 0:
        print("I valgte det samme. Det står derfor ulige.")

    if choose == "2" and randomint == 0:
        print("Du tabte desværre!")
    elif choose == "2" and randomint == 2:
        print("Tillykke! Du vandt.")
    elif choose == "2" and randomint == 1:
        print("I valgte det samme. Det står derfor ulige.")

    if choose == "3" and randomint == 1:
        print("Du tabte desværre!")
    elif choose == "3" and randomint == 0:
        print("Tillykke! Du vandt.")
    elif choose == "3" and randomint == 2:
        print("I valgte det samme. Det står derfor lige.")

    time.sleep(3)

    tryagain = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTryk Enter, hvis du ønsker at prøve igen.\n\n\n\n\n")
    
    if tryagain != "":
        webbrowser.open_new("https://www.youtube.com/watch?v=xvFZjo5PgG0")
        quit()
    elif tryagain == "":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")