from os import system, name
import walka
import random
import time
import funkcje 
import sys
import napisy
import fabula

def menug():
    funkcje.agwiazdki()
    funkcje.delay_print("FLEXOLIA 1.0.1\n")
    funkcje.agwiazdki()
    time.sleep(0.7)
    print("\nMenu:")
    time.sleep(0.7)
    print("1. Start")
    time.sleep(0.7)
    print("2. Opcje")
    time.sleep(0.7)
    print("3. Napisy\n")
    menu = int(input())

    funkcje.clear()

    if menu == 1:
        exp = funkcje.startgry()
        if exp > 30:
            fabula.fabulazakonczenie()
            funkcje.clear()
        else:
            fabula.fabulazlezakonczenie()              
    elif menu == 2:
        funkcje.clear()
        print("*******************************************")
        print("DŹWIĘK: brak")
        print("*******************************************")
        time.sleep(0.3)
        print("GRAFIKA: brak")
        print("*******************************************")
        time.sleep(0.3)
        print("STEROWNIE: brak")
        print("*******************************************")
        time.sleep(0.3)
        back = int(input("0. Powrót\n"))
        if back == 0:
            funkcje.clear()
            menug()
        else:
            funkcje.clear()
            menug()
    elif menu == 3:
        napisy.runnapisy()            
    else:
        menug()
    napisy.runnapisy()
