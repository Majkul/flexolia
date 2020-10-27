from os import system, name
import walka
import time
import funkcje

dlcmag = 0
dlclowca = 0

def dlcczarnamagia():
    global dlcmag
    if dlcmag == 0:
        funkcje.clear()
        print("*******************************************")
        print("Kup DLC \"Czarna Magia\" za 164.98 PLN aby odblokować postać.")
        print("*******************************************")
        time.sleep(0.5)
        print("\nJeżeli zakupiłeś już DLC, wpisz kod aktywacyjny.")
        time.sleep(0.3)
        print("Jeśli nie, wpisz 0 aby wrócić.\n")
        kod = str(input())
        if kod == "BlckMaGcCUwU":
            funkcje.clear()
            time.sleep(0.3)
            print("Aktywowałeś DLC \"Czarna Magia\"!")
            time.sleep(0.3)
            print("Wybierz klasę \"Mag\" w menu wyboru klasy aby przetestować postać.")
            dlcmag = int(1)
            time.sleep(0.3)
            back = int(input("\n0. Powrót\n"))
            if back == 0:
                funkcje.clear()
                funkcje.startgry()
            else:
                funkcje.clear()
                funkcje.startgry()
        elif kod == "0":
            funkcje.clear()
            funkcje.startgry()
        else:
            funkcje.clear()
            time.sleep(0.3)
            print("Niewłaściwy kod.")
            time.sleep(2.0)
            funkcje.clear()
            funkcje.startgry()
    elif dlcmag == 1:
        exp = walka.Walka.magork()
        funkcje.clear()
        exp2 = walka.Walka.magwilki()
        exp += exp2
        funkcje.clear()
        exp3 = walka.Walka.maggolem()
        exp += exp3
        funkcje.clear()
        return exp
    else:
        print("ERROR")
    

def dlclowcaglow():
    global dlclowca
    if dlclowca == 0:
        funkcje.clear()
        print("*******************************************")
        print("Kup DLC \"Łowca Głów\" za 164.98 PLN aby odblokować postać.")
        print("*******************************************")
        time.sleep(0.5)
        print("\nJeżeli zakupiłeś już DLC, wpisz kod aktywacyjny.")
        time.sleep(0.3)
        print("Jeśli nie, wpisz 0 aby wrócić.\n")
        kod = str(input())
        if kod == "7uKg0brRrRR":
            funkcje.clear()
            time.sleep(0.3)
            print("Aktywowałeś DLC \"Łowca Głów\"!")
            time.sleep(0.3)
            print("Wybierz klasę \"Łowca\" w menu wyboru klasy aby przetestować postać.")
            dlclowca = int(1)
            time.sleep(0.3)
            back = int(input("\n0. Powrót\n"))
            if back == 0:
                funkcje.clear()
                funkcje.startgry()
            else:
                funkcje.clear()
                funkcje.startgry()
        elif kod == "0":
            funkcje.clear()
            funkcje.startgry()
        else:
            funkcje.clear()
            time.sleep(0.3)
            print("Niewłaściwy kod.")
            time.sleep(2.0)
            funkcje.clear()
            funkcje.startgry()
    elif dlclowca == 1:
        exp = walka.Walka.lowcaork()
        funkcje.clear()
        exp2 = walka.Walka.lowcawilki()
        exp += exp2
        funkcje.clear()
        exp3 = walka.Walka.lowcagolem()
        exp += exp3
        funkcje.clear()
        return exp
    else:
        print("ERROR")