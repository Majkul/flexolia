from os import system, name
import walka
import time
import sys
import dlcs
import funkcje
import menuglowne

def runnapisy():
    funkcje.clear()
    funkcje.agwiazdki()
    print("")
    time.sleep(0.3)
    funkcje.delay_print("FLEXOLIA\n\n")
    time.sleep(0.3)
    funkcje.agwiazdki()
    print("")
    time.sleep(0.7)
    print("Oprogramowanie")
    time.sleep(0.3)
    print("")
    time.sleep(0.3)
    print("Michał Sołowiej")
    time.sleep(0.3)
    print("Kornel Świerzbiński")
    time.sleep(0.3)
    funkcje.przewijanie()
    print("Pomysły")
    time.sleep(0.3)
    print("")
    time.sleep(0.3)
    print("Michał Sołowiej")
    time.sleep(0.3)
    print("Kornel Świerzbiński")
    time.sleep(0.3)
    print("Oliwier Niemotko")
    time.sleep(0.3)
    funkcje.przewijanie()
    print("Dźwięk")
    time.sleep(0.3)
    funkcje.przewijanie()
    print("Grafika")
    time.sleep(0.3)
    funkcje.przewijanie()
    print("Dubbing")
    time.sleep(0.3)
    funkcje.przewijanie()
    print("Tłumaczenie")
    time.sleep(0.3)
    funkcje.przewijanie()
    print("Sponsorzy")
    time.sleep(0.3)
    funkcje.przewijanie()
    funkcje.przewijanie()
    funkcje.przewijanie()
    funkcje.przewijanie()
    funkcje.przewijanie()
    time.sleep(0.3)    
    back = int(input("0. Powrót\n"))
    if back == 0:
        funkcje.clear()
        menuglowne.menug()    
    else:
       funkcje.clear()
       menuglowne.menug()