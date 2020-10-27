from os import system, name
import walka
import time
import sys
import dlcs
import fabula
import menuglowne

exp = 0

def clear(): 
    
    if name == 'nt': 
        _ = system('cls') 


def startgry():
    global exp
    print("*******************************************")
    print("Wybierz klase postaci")
    print("*******************************************")
    time.sleep(0.3)
    print("1. Wojownik")
    time.sleep(0.3)
    print("2. Mag")
    time.sleep(0.3)
    print("3. Łowca")
    print("*******************************************")
    time.sleep(0.3)
    klasa = int(input())
    clear()
    if klasa == 1:
        exp = walka.Walka.wojownikork()
        clear()
        exp2 = walka.Walka.wojownikwilki()
        exp += exp2
        clear()
        exp3 = walka.Walka.wojownikgolem()
        exp += exp3
        clear()
    elif klasa == 2:
        dlcs.dlcczarnamagia()
    elif klasa == 3:
        dlcs.dlclowcaglow()
        clear()
    else:
        startgry()
    return exp

def przewijanie():

    tekst = 0
    while tekst < 10:
        tekst = tekst + 1
        print("")
        time.sleep(0.3)

def agwiazdki():
    animation = ["*"]

    for i in range(43):
        time.sleep(0.03)
        sys.stdout.write(animation[i % len(animation)])
        sys.stdout.flush()
    print("")

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

