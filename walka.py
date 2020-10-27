import random
import time
import funkcje
import fabula
import sys
import dlcs
import menuglowne

class Walka():
    def wojownikork():
        fabula.fabulastart()
        exp = int()
        print("*******************************************")
        print("Spotykasz na drodze orka")
        time.sleep(0.3)
        print("Co robisz?")
        print("*******************************************")
        time.sleep(0.3)
        print("1. Podejmuje walkę")
        time.sleep(0.3)
        print("2. Uciekam (- 10 PD)")
        walka = int(input())
        funkcje.clear()
        time.sleep(0.3)
        if walka == 1:
            hporka = float(50)
            hpg = float(60) 
            while hporka > 0 and hpg > 0 :
                print("*******************************************")
                print("Twoje życie = " + str(hpg))
                time.sleep(0.1)
                print("")
                time.sleep(0.1)
                print("Życie orka = " + str(hporka))
                print("*******************************************")
                time.sleep(0.1)
                print("Wybierz atak:")
                print("*******************************************")
                time.sleep(0.1)
                print("1. Prosty atak (10 - 15 DMG)")
                time.sleep(0.1)
                print("2. Dźgnięcie i blok (4 DMG) [blokuje 50% DMG]")
                atak = int(input())
                if atak == 1:
                    multiplierwroga = int(1)
                    zadanydmg = float(random.randrange(10, 15))
                    dostanydmg = float(random.randrange(9, 12))
                    hporka = float(hporka - zadanydmg)
                    if hporka > 0:
                        hpg = float(hpg - dostanydmg)
                        print("*******************************************")
                        print("Zadałeś Orkowi " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Ork zadał ci " + str(dostanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                    else:
                        print("*******************************************")
                        print("Zadałeś Orkowi " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Ork zmarł zanim zaatakował")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                elif atak == 2:
                    multiplierwroga = float(0.5)
                    zadanydmg = float(4)
                    dostanydmg = float(random.randrange(9, 12))
                    hporka = hporka - zadanydmg
                    if hporka > 0:
                        hpg = float(hpg - dostanydmg * multiplierwroga)
                        print("*******************************************")
                        print("Zadałeś Orkowi " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Ork zadał ci " + str(dostanydmg * multiplierwroga) + " DMG")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                    else:
                        print("*******************************************")
                        print("Zadałeś Orkowi " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Ork zmarł zanim zaatakował")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                else:
                    funkcje.clear()
                    print("Niewłaściwy atak.") 
                    time.sleep(1.3) 
                    funkcje.clear()

            if hpg >= 0 and hporka <= 0:
                print("*******************************************")
                print("Ork poległ.")
                time.sleep(0.3)
                print("Dostajesz 30 PD.")
                print("*******************************************")
                exp = exp + 30
                time.sleep(5)
            elif hporka >= 0 and hpg <= 0:
                print("*******************************************")
                print("Ork wygrał.")
                time.sleep(0.3)
                print("Tracisz 15 PD.")
                print("*******************************************")
                exp = exp - 15
                time.sleep(5)
            else: 
                print("ERROR")
        elif walka == 2:
            print("Omijasz Orka. (- 10 PD)")
            time.sleep(5)
            exp = exp - 10
        return exp

    def wojownikwilki():
        exp = int()
        print("*******************************************")
        print("Spotykasz na drodze watahę wilków")
        time.sleep(0.3)
        print("Co robisz?")
        print("*******************************************")
        time.sleep(0.3)
        print("1. Podejmuje walkę")
        time.sleep(0.3)
        print("2. Uciekam (- 10 PD)")
        walka = int(input())
        funkcje.clear()
        time.sleep(0.3)
        if walka == 1:
            hpwilka = float(40)
            hpg = float(60) 
            while hpwilka > 0 and hpg > 0 :
                print("*******************************************")
                print("Twoje życie = " + str(hpg))
                time.sleep(0.1)
                print("")
                time.sleep(0.1)
                print("Życie wilków = " + str(hpwilka))
                print("*******************************************")
                time.sleep(0.1)
                print("Wybierz atak:")
                print("*******************************************")
                time.sleep(0.1)
                print("1. Prosty atak (10 - 15 DMG)")
                time.sleep(0.1)
                print("2. Dźgnięcie i blok (4 DMG) [blokuje 50% DMG]")
                atak = int(input())
                if atak == 1:
                    multiplierwroga = int(1)
                    zadanydmg = float(random.randrange(10, 15))
                    dostanydmg = float(random.randrange(7, 10))
                    hpwilka = float(hpwilka - zadanydmg)
                    if hpwilka > 0:
                        hpg = float(hpg - dostanydmg)
                        print("*******************************************")
                        print("Zadałeś wilkom " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Wilki zadały ci " + str(dostanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                    else:
                        print("*******************************************")
                        print("Zadałeś wilkom " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Wilki zmarły zanim zaatakowały")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                elif atak == 2:
                    multiplierwroga = float(0.5)
                    zadanydmg = float(4)
                    dostanydmg = float(random.randrange(9, 12))
                    hpwilka = hpwilka - zadanydmg
                    if hpwilka > 0:
                        hpg = float(hpg - dostanydmg * multiplierwroga)
                        print("*******************************************")
                        print("Zadałeś wilkom " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Wilki zadały ci " + str(dostanydmg * multiplierwroga) + " DMG")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                    else:
                        print("*******************************************")
                        print("Zadałeś wilkom " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Wilki zmarły zanim zaatakowały")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                else:
                    funkcje.clear()
                    print("Niewłaściwy atak.") 
                    time.sleep(1.3) 
                    funkcje.clear()

            if hpg >= 0 and hpwilka <= 0:
                print("*******************************************")
                print("Wilki poległy.")
                time.sleep(0.3)
                print("Dostajesz 25 PD.")
                print("*******************************************")
                exp = exp + 25
                time.sleep(5)
            elif hpwilka >= 0 and hpg <= 0:
                print("*******************************************")
                print("Wilki wygrały.")
                time.sleep(0.3)
                print("Tracisz 13 PD.")
                print("*******************************************")
                exp = exp - 13
                time.sleep(5)
            else: 
                print("ERROR")
        elif walka == 2:
            print("Omijasz wilki. (- 10 PD)")
            time.sleep(5)
            exp = exp - 10
        return exp

    def wojownikgolem():
        exp = int()
        print("*******************************************")
        print("Spotykasz na drodze Golema")
        time.sleep(0.3)
        print("Co robisz?")
        print("*******************************************")
        time.sleep(0.3)
        print("1. Podejmuje walkę")
        time.sleep(0.3)
        print("2. Uciekam (- 10 PD)")
        walka = int(input())
        funkcje.clear()
        time.sleep(0.3)
        if walka == 1:
            hpgolem = float(70)
            hpg = float(60) 
            while hpgolem > 0 and hpg > 0 :
                print("*******************************************")
                print("Twoje życie = " + str(hpg))
                time.sleep(0.1)
                print("")
                time.sleep(0.1)
                print("Życie Golema = " + str(hpgolem))
                print("*******************************************")
                time.sleep(0.1)
                print("Wybierz atak:")
                print("*******************************************")
                time.sleep(0.1)
                print("1. Prosty atak (10 - 15 DMG)")
                time.sleep(0.1)
                print("2. Dźgnięcie i blok (4 DMG) [blokuje 50% DMG]")
                atak = int(input())
                if atak == 1:
                    multiplierwroga = int(1)
                    zadanydmg = float(random.randrange(10, 15))
                    dostanydmg = float(random.randrange(6, 9))
                    hpgolem = float(hpgolem - zadanydmg)
                    if hpgolem > 0:
                        hpg = float(hpg - dostanydmg)
                        print("*******************************************")
                        print("Zadałeś Golemowi " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Golem zadał ci " + str(dostanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                    else:
                        print("*******************************************")
                        print("Zadałeś Golemowi " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Golemo zmarł zanim zaatakował")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                elif atak == 2:
                    multiplierwroga = float(0.5)
                    zadanydmg = float(4)
                    dostanydmg = float(random.randrange(9, 12))
                    hpgolem = hpgolem - zadanydmg
                    if hpgolem > 0:
                        hpg = float(hpg - dostanydmg * multiplierwroga)
                        print("*******************************************")
                        print("Zadałeś Golemowi " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Golemo zadał ci " + str(dostanydmg * multiplierwroga) + " DMG")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                    else:
                        print("*******************************************")
                        print("Zadałeś Golemowi " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Golemo zmarł zanim zaatakował")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                else:
                    funkcje.clear()
                    print("Niewłaściwy atak.") 
                    time.sleep(1.3) 
                    funkcje.clear()

            if hpg >= 0 and hpgolem <= 0:
                print("*******************************************")
                print("Golemo poległ.")
                time.sleep(0.3)
                print("Dostajesz 25 PD.")
                print("*******************************************")
                exp = exp + 25
                time.sleep(5)
            elif hpgolem >= 0 and hpg <= 0:
                print("*******************************************")
                print("Golem wygrały.")
                time.sleep(0.3)
                print("Tracisz 15 PD.")
                print("*******************************************")
                exp = exp - 15
                time.sleep(5)
            else: 
                print("ERROR")
        elif walka == 2:
            print("Omijasz Golema. (- 10 PD)")
            time.sleep(5)
            exp = exp - 10
        return exp        


    def magork():
            fabula.fabulastart()
            exp = int()
            print("*******************************************")
            print("Spotykasz na drodze orka")
            time.sleep(0.3)
            print("Co robisz?")
            print("*******************************************")
            time.sleep(0.3)
            print("1. Podejmuje walkę")
            time.sleep(0.3)
            print("2. Uciekam (- 10 PD)")
            walka = int(input())
            funkcje.clear()
            time.sleep(0.3)
            if walka == 1:
                hporka = float(50)
                hpg = float(45) 
                while hporka > 0 and hpg > 0 :
                    print("*******************************************")
                    print("Twoje życie = " + str(hpg))
                    time.sleep(0.1)
                    print("")
                    time.sleep(0.1)
                    print("Życie orka = " + str(hporka))
                    print("*******************************************")
                    time.sleep(0.1)
                    print("Wybierz atak:")
                    print("*******************************************")
                    time.sleep(0.1)
                    print("1. Proste zaklęcie  (12 - 21 DMG)")
                    time.sleep(0.1)
                    print("2. Firewall (8 DMG) [blokuje 50% DMG]")
                    atak = int(input())
                    if atak == 1:
                        multiplierwroga = int(1)
                        zadanydmg = float(random.randrange(12, 21))
                        dostanydmg = float(random.randrange(9, 12))
                        hporka = float(hporka - zadanydmg)
                        if hporka > 0:
                            hpg = float(hpg - dostanydmg)
                            print("*******************************************")
                            print("Zadałeś Orkowi " + str(zadanydmg) + " DMG")
                            print("*******************************************")
                            time.sleep(0.2)
                            print("Ork zadał ci " + str(dostanydmg) + " DMG")
                            print("*******************************************")
                            time.sleep(1.3)
                            funkcje.clear()
                        else:
                            print("*******************************************")
                            print("Zadałeś Orkowi " + str(zadanydmg) + " DMG")
                            print("*******************************************")
                            time.sleep(0.2)
                            print("Ork zmarł zanim zaatakował")
                            print("*******************************************")
                            time.sleep(1.3)
                            funkcje.clear()
                    elif atak == 2:
                        multiplierwroga = float(0.5)
                        zadanydmg = float(4)
                        dostanydmg = float(random.randrange(9, 12))
                        hporka = hporka - zadanydmg
                        if hporka > 0:
                            hpg = float(hpg - dostanydmg * multiplierwroga)
                            print("*******************************************")
                            print("Zadałeś Orkowi " + str(zadanydmg) + " DMG")
                            print("*******************************************")
                            time.sleep(0.2)
                            print("Ork zadał ci " + str(dostanydmg * multiplierwroga) + " DMG")
                            print("*******************************************")
                            time.sleep(1.3)
                            funkcje.clear()
                        else:
                            print("*******************************************")
                            print("Zadałeś Orkowi " + str(zadanydmg) + " DMG")
                            print("*******************************************")
                            time.sleep(0.2)
                            print("Ork zmarł zanim zaatakował")
                            print("*******************************************")
                            time.sleep(1.3)
                            funkcje.clear()
                    else:
                        funkcje.clear()
                        print("Niewłaściwy atak.") 
                        time.sleep(1.3) 
                        funkcje.clear()

                if hpg >= 0 and hporka <= 0:
                    print("*******************************************")
                    print("Ork poległ.")
                    time.sleep(0.3)
                    print("Dostajesz 30 PD.")
                    print("*******************************************")
                    exp = exp + 30
                    time.sleep(5)
                elif hporka >= 0 and hpg <= 0:
                    print("*******************************************")
                    print("Ork wygrał.")
                    time.sleep(0.3)
                    print("Tracisz 15 PD.")
                    print("*******************************************")
                    exp = exp - 15
                    time.sleep(5)
                else: 
                    print("ERROR")
            elif walka == 2:
                print("Omijasz Orka. (- 10 PD)")
                time.sleep(5)
                exp = exp - 10
            return exp


    def magwilki():
        exp = int()
        print("*******************************************")
        print("Spotykasz na drodze watahę wilków")
        time.sleep(0.3)
        print("Co robisz?")
        print("*******************************************")
        time.sleep(0.3)
        print("1. Podejmuje walkę")
        time.sleep(0.3)
        print("2. Uciekam (- 10 PD)")
        walka = int(input())
        funkcje.clear()
        time.sleep(0.3)
        if walka == 1:
            hpwilka = float(40)
            hpg = float(45) 
            while hpwilka > 0 and hpg > 0 :
                print("*******************************************")
                print("Twoje życie = " + str(hpg))
                time.sleep(0.1)
                print("")
                time.sleep(0.1)
                print("Życie wilków = " + str(hpwilka))
                print("*******************************************")
                time.sleep(0.1)
                print("Wybierz atak:")
                print("*******************************************")
                time.sleep(0.1)
                print("1. Proste zaklęcie (12 - 21 DMG)")
                time.sleep(0.1)
                print("2. Firewall (4 DMG) [blokuje 50% DMG]")
                atak = int(input())
                if atak == 1:
                    multiplierwroga = int(1)
                    zadanydmg = float(random.randrange(12, 21))
                    dostanydmg = float(random.randrange(7, 10))
                    hpwilka = float(hpwilka - zadanydmg)
                    if hpwilka > 0:
                        hpg = float(hpg - dostanydmg)
                        print("*******************************************")
                        print("Zadałeś wilkom " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Wilki zadały ci " + str(dostanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                    else:
                        print("*******************************************")
                        print("Zadałeś wilkom " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Wilki zmarły zanim zaatakowały")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                elif atak == 2:
                    multiplierwroga = float(0.5)
                    zadanydmg = float(4)
                    dostanydmg = float(random.randrange(9, 12))
                    hpwilka = hpwilka - zadanydmg
                    if hpwilka > 0:
                        hpg = float(hpg - dostanydmg * multiplierwroga)
                        print("*******************************************")
                        print("Zadałeś wilkom " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Wilki zadały ci " + str(dostanydmg * multiplierwroga) + " DMG")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                    else:
                        print("*******************************************")
                        print("Zadałeś wilkom " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Wilki zmarły zanim zaatakowały")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                else:
                    funkcje.clear()
                    print("Niewłaściwy atak.") 
                    time.sleep(1.3) 
                    funkcje.clear()

            if hpg >= 0 and hpwilka <= 0:
                print("*******************************************")
                print("Wilki poległy.")
                time.sleep(0.3)
                print("Dostajesz 25 PD.")
                print("*******************************************")
                exp = exp + 25
                time.sleep(5)
            elif hpwilka >= 0 and hpg <= 0:
                print("*******************************************")
                print("Wilki wygrały.")
                time.sleep(0.3)
                print("Tracisz 13 PD.")
                print("*******************************************")
                exp = exp - 13
                time.sleep(5)
            else: 
                print("ERROR")
        elif walka == 2:
            print("Omijasz wilki. (- 10 PD)")
            time.sleep(5)
            exp = exp - 10
        return exp


    def maggolem():
        exp = int()
        print("*******************************************")
        print("Spotykasz na drodze Golema")
        time.sleep(0.3)
        print("Co robisz?")
        print("*******************************************")
        time.sleep(0.3)
        print("1. Podejmuje walkę")
        time.sleep(0.3)
        print("2. Uciekam (- 10 PD)")
        walka = int(input())
        funkcje.clear()
        time.sleep(0.3)
        if walka == 1:
            hpgolem = float(70)
            hpg = float(45) 
            while hpgolem > 0 and hpg > 0 :
                print("*******************************************")
                print("Twoje życie = " + str(hpg))
                time.sleep(0.1)
                print("")
                time.sleep(0.1)
                print("Życie Golema = " + str(hpgolem))
                print("*******************************************")
                time.sleep(0.1)
                print("Wybierz atak:")
                print("*******************************************")
                time.sleep(0.1)
                print("1. Proste zaklęcie (12 - 21 DMG)")
                time.sleep(0.1)
                print("2. Firewall (4 DMG) [blokuje 50% DMG]")
                atak = int(input())
                if atak == 1:
                    multiplierwroga = int(1)
                    zadanydmg = float(random.randrange(12, 21))
                    dostanydmg = float(random.randrange(6, 9))
                    hpgolem = float(hpgolem - zadanydmg)
                    if hpgolem > 0:
                        hpg = float(hpg - dostanydmg)
                        print("*******************************************")
                        print("Zadałeś Golemowi " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Golem zadał ci " + str(dostanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                    else:
                        print("*******************************************")
                        print("Zadałeś Golemowi " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Golemo zmarł zanim zaatakował")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                elif atak == 2:
                    multiplierwroga = float(0.5)
                    zadanydmg = float(4)
                    dostanydmg = float(random.randrange(9, 12))
                    hpgolem = hpgolem - zadanydmg
                    if hpgolem > 0:
                        hpg = float(hpg - dostanydmg * multiplierwroga)
                        print("*******************************************")
                        print("Zadałeś Golemowi " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Golemo zadał ci " + str(dostanydmg * multiplierwroga) + " DMG")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                    else:
                        print("*******************************************")
                        print("Zadałeś Golemowi " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Golemo zmarł zanim zaatakował")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                else:
                    funkcje.clear()
                    print("Niewłaściwy atak.") 
                    time.sleep(1.3) 
                    funkcje.clear()

            if hpg >= 0 and hpgolem <= 0:
                print("*******************************************")
                print("Golemo poległ.")
                time.sleep(0.3)
                print("Dostajesz 25 PD.")
                print("*******************************************")
                exp = exp + 25
                time.sleep(5)
            elif hpgolem >= 0 and hpg <= 0:
                print("*******************************************")
                print("Golem wygrały.")
                time.sleep(0.3)
                print("Tracisz 15 PD.")
                print("*******************************************")
                exp = exp - 15
                time.sleep(5)
            else: 
                print("ERROR")
        elif walka == 2:
            print("Omijasz Golema. (- 10 PD)")
            time.sleep(5)
            exp = exp - 10
        return exp  

    def magork():
            fabula.fabulastart()
            exp = int()
            print("*******************************************")
            print("Spotykasz na drodze orka")
            time.sleep(0.3)
            print("Co robisz?")
            print("*******************************************")
            time.sleep(0.3)
            print("1. Podejmuje walkę")
            time.sleep(0.3)
            print("2. Uciekam (- 10 PD)")
            walka = int(input())
            funkcje.clear()
            time.sleep(0.3)
            if walka == 1:
                hporka = float(50)
                hpg = float(45) 
                while hporka > 0 and hpg > 0 :
                    print("*******************************************")
                    print("Twoje życie = " + str(hpg))
                    time.sleep(0.1)
                    print("")
                    time.sleep(0.1)
                    print("Życie orka = " + str(hporka))
                    print("*******************************************")
                    time.sleep(0.1)
                    print("Wybierz atak:")
                    print("*******************************************")
                    time.sleep(0.1)
                    print("1. Proste zaklęcie  (12 - 21 DMG)")
                    time.sleep(0.1)
                    print("2. Firewall (8 DMG) [blokuje 50% DMG]")
                    atak = int(input())
                    if atak == 1:
                        multiplierwroga = int(1)
                        zadanydmg = float(random.randrange(12, 21))
                        dostanydmg = float(random.randrange(9, 12))
                        hporka = float(hporka - zadanydmg)
                        if hporka > 0:
                            hpg = float(hpg - dostanydmg)
                            print("*******************************************")
                            print("Zadałeś Orkowi " + str(zadanydmg) + " DMG")
                            print("*******************************************")
                            time.sleep(0.2)
                            print("Ork zadał ci " + str(dostanydmg) + " DMG")
                            print("*******************************************")
                            time.sleep(1.3)
                            funkcje.clear()
                        else:
                            print("*******************************************")
                            print("Zadałeś Orkowi " + str(zadanydmg) + " DMG")
                            print("*******************************************")
                            time.sleep(0.2)
                            print("Ork zmarł zanim zaatakował")
                            print("*******************************************")
                            time.sleep(1.3)
                            funkcje.clear()
                    elif atak == 2:
                        multiplierwroga = float(0.5)
                        zadanydmg = float(4)
                        dostanydmg = float(random.randrange(9, 12))
                        hporka = hporka - zadanydmg
                        if hporka > 0:
                            hpg = float(hpg - dostanydmg * multiplierwroga)
                            print("*******************************************")
                            print("Zadałeś Orkowi " + str(zadanydmg) + " DMG")
                            print("*******************************************")
                            time.sleep(0.2)
                            print("Ork zadał ci " + str(dostanydmg * multiplierwroga) + " DMG")
                            print("*******************************************")
                            time.sleep(1.3)
                            funkcje.clear()
                        else:
                            print("*******************************************")
                            print("Zadałeś Orkowi " + str(zadanydmg) + " DMG")
                            print("*******************************************")
                            time.sleep(0.2)
                            print("Ork zmarł zanim zaatakował")
                            print("*******************************************")
                            time.sleep(1.3)
                            funkcje.clear()
                    else:
                        funkcje.clear()
                        print("Niewłaściwy atak.") 
                        time.sleep(1.3) 
                        funkcje.clear()

                if hpg >= 0 and hporka <= 0:
                    print("*******************************************")
                    print("Ork poległ.")
                    time.sleep(0.3)
                    print("Dostajesz 30 PD.")
                    print("*******************************************")
                    exp = exp + 30
                    time.sleep(5)
                elif hporka >= 0 and hpg <= 0:
                    print("*******************************************")
                    print("Ork wygrał.")
                    time.sleep(0.3)
                    print("Tracisz 15 PD.")
                    print("*******************************************")
                    exp = exp - 15
                    time.sleep(5)
                else: 
                    print("ERROR")
            elif walka == 2:
                print("Omijasz Orka. (- 10 PD)")
                time.sleep(5)
                exp = exp - 10
            return exp


    def magwilki():
        exp = int()
        print("*******************************************")
        print("Spotykasz na drodze watahę wilków")
        time.sleep(0.3)
        print("Co robisz?")
        print("*******************************************")
        time.sleep(0.3)
        print("1. Podejmuje walkę")
        time.sleep(0.3)
        print("2. Uciekam (- 10 PD)")
        walka = int(input())
        funkcje.clear()
        time.sleep(0.3)
        if walka == 1:
            hpwilka = float(40)
            hpg = float(45) 
            while hpwilka > 0 and hpg > 0 :
                print("*******************************************")
                print("Twoje życie = " + str(hpg))
                time.sleep(0.1)
                print("")
                time.sleep(0.1)
                print("Życie wilków = " + str(hpwilka))
                print("*******************************************")
                time.sleep(0.1)
                print("Wybierz atak:")
                print("*******************************************")
                time.sleep(0.1)
                print("1. Proste zaklęcie (12 - 21 DMG)")
                time.sleep(0.1)
                print("2. Firewall (4 DMG) [blokuje 50% DMG]")
                atak = int(input())
                if atak == 1:
                    multiplierwroga = int(1)
                    zadanydmg = float(random.randrange(12, 21))
                    dostanydmg = float(random.randrange(7, 10))
                    hpwilka = float(hpwilka - zadanydmg)
                    if hpwilka > 0:
                        hpg = float(hpg - dostanydmg)
                        print("*******************************************")
                        print("Zadałeś wilkom " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Wilki zadały ci " + str(dostanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                    else:
                        print("*******************************************")
                        print("Zadałeś wilkom " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Wilki zmarły zanim zaatakowały")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                elif atak == 2:
                    multiplierwroga = float(0.5)
                    zadanydmg = float(4)
                    dostanydmg = float(random.randrange(9, 12))
                    hpwilka = hpwilka - zadanydmg
                    if hpwilka > 0:
                        hpg = float(hpg - dostanydmg * multiplierwroga)
                        print("*******************************************")
                        print("Zadałeś wilkom " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Wilki zadały ci " + str(dostanydmg * multiplierwroga) + " DMG")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                    else:
                        print("*******************************************")
                        print("Zadałeś wilkom " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Wilki zmarły zanim zaatakowały")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                else:
                    funkcje.clear()
                    print("Niewłaściwy atak.") 
                    time.sleep(1.3) 
                    funkcje.clear()

            if hpg >= 0 and hpwilka <= 0:
                print("*******************************************")
                print("Wilki poległy.")
                time.sleep(0.3)
                print("Dostajesz 25 PD.")
                print("*******************************************")
                exp = exp + 25
                time.sleep(5)
            elif hpwilka >= 0 and hpg <= 0:
                print("*******************************************")
                print("Wilki wygrały.")
                time.sleep(0.3)
                print("Tracisz 13 PD.")
                print("*******************************************")
                exp = exp - 13
                time.sleep(5)
            else: 
                print("ERROR")
        elif walka == 2:
            print("Omijasz wilki. (- 10 PD)")
            time.sleep(5)
            exp = exp - 10
        return exp


    def maggolem():
        exp = int()
        print("*******************************************")
        print("Spotykasz na drodze Golema")
        time.sleep(0.3)
        print("Co robisz?")
        print("*******************************************")
        time.sleep(0.3)
        print("1. Podejmuje walkę")
        time.sleep(0.3)
        print("2. Uciekam (- 10 PD)")
        walka = int(input())
        funkcje.clear()
        time.sleep(0.3)
        if walka == 1:
            hpgolem = float(70)
            hpg = float(45) 
            while hpgolem > 0 and hpg > 0 :
                print("*******************************************")
                print("Twoje życie = " + str(hpg))
                time.sleep(0.1)
                print("")
                time.sleep(0.1)
                print("Życie Golema = " + str(hpgolem))
                print("*******************************************")
                time.sleep(0.1)
                print("Wybierz atak:")
                print("*******************************************")
                time.sleep(0.1)
                print("1. Proste zaklęcie (12 - 21 DMG)")
                time.sleep(0.1)
                print("2. Firewall (4 DMG) [blokuje 50% DMG]")
                atak = int(input())
                if atak == 1:
                    multiplierwroga = int(1)
                    zadanydmg = float(random.randrange(12, 21))
                    dostanydmg = float(random.randrange(6, 9))
                    hpgolem = float(hpgolem - zadanydmg)
                    if hpgolem > 0:
                        hpg = float(hpg - dostanydmg)
                        print("*******************************************")
                        print("Zadałeś Golemowi " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Golem zadał ci " + str(dostanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                    else:
                        print("*******************************************")
                        print("Zadałeś Golemowi " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Golemo zmarł zanim zaatakował")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                elif atak == 2:
                    multiplierwroga = float(0.5)
                    zadanydmg = float(4)
                    dostanydmg = float(random.randrange(9, 12))
                    hpgolem = hpgolem - zadanydmg
                    if hpgolem > 0:
                        hpg = float(hpg - dostanydmg * multiplierwroga)
                        print("*******************************************")
                        print("Zadałeś Golemowi " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Golemo zadał ci " + str(dostanydmg * multiplierwroga) + " DMG")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                    else:
                        print("*******************************************")
                        print("Zadałeś Golemowi " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Golemo zmarł zanim zaatakował")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                else:
                    funkcje.clear()
                    print("Niewłaściwy atak.") 
                    time.sleep(1.3) 
                    funkcje.clear()

            if hpg >= 0 and hpgolem <= 0:
                print("*******************************************")
                print("Golemo poległ.")
                time.sleep(0.3)
                print("Dostajesz 25 PD.")
                print("*******************************************")
                exp = exp + 25
                time.sleep(5)
            elif hpgolem >= 0 and hpg <= 0:
                print("*******************************************")
                print("Golem wygrały.")
                time.sleep(0.3)
                print("Tracisz 15 PD.")
                print("*******************************************")
                exp = exp - 15
                time.sleep(5)
            else: 
                print("ERROR")
        elif walka == 2:
            print("Omijasz Golema. (- 10 PD)")
            time.sleep(5)
            exp = exp - 10
        return exp      


    def lowcaork():
        fabula.fabulastart()
        exp = int()
        print("*******************************************")
        print("Spotykasz na drodze orka")
        time.sleep(0.3)
        print("Co robisz?")
        print("*******************************************")
        time.sleep(0.3)
        print("1. Podejmuje walkę")
        time.sleep(0.3)
        print("2. Uciekam (- 10 PD)")
        walka = int(input())
        funkcje.clear()
        time.sleep(0.3)
        if walka == 1:
            hporka = float(50)
            hpg = float(55) 
            while hporka > 0 and hpg > 0 :
                print("*******************************************")
                print("Twoje życie = " + str(hpg))
                time.sleep(0.1)
                print("")
                time.sleep(0.1)
                print("Życie orka = " + str(hporka))
                print("*******************************************")
                time.sleep(0.1)
                print("Wybierz atak:")
                print("*******************************************")
                time.sleep(0.1)
                print("1. Strzał z łuku  (10 - 12 DMG)")
                time.sleep(0.1)
                print("2. Unik (redukuje 100% otrzymanego DMG)")
                atak = int(input())
                if atak == 1:
                    multiplierwroga = int(1)
                    t = float(random.randrange(1, 5))
                    if t == 1:
                        zadanydmg = 0
                        print("*******************************************")
                        print("Nie trafiłeś")
                        print("*******************************************")
                        time.sleep(0.6)
                    elif t == 2 or 3 or 4:
                        zadanydmg = float(random.randrange(10, 12))
                        print("*******************************************")
                        print("Trafiłeś")
                        print("*******************************************")
                        time.sleep(0.6)
                    else:
                        zadanydmg = float(random.randrange(15, 18))
                        print("*******************************************")
                        print("Trafiłeś w głowę")
                        print("*******************************************")
                        time.sleep(0.6)
                    dostanydmg = float(random.randrange(9, 12))
                    hporka = float(hporka - zadanydmg)
                    if hporka > 0:
                        hpg = float(hpg - dostanydmg)
                        print("Zadałeś Orkowi " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Ork zadał ci " + str(dostanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                    else:
                        print("Zadałeś Orkowi " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Ork zmarł zanim zaatakował")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                elif atak == 2:
                    multiplierwroga = 0
                    zadanydmg = 0
                    dostanydmg = 0
                    hporka = hporka - zadanydmg
                    if hporka > 0:
                        hpg = float(hpg - dostanydmg * multiplierwroga)
                        print("Zadałeś Orkowi " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Ork zadał ci " + str(dostanydmg * multiplierwroga) + " DMG")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                    else:
                        print("Zadałeś Orkowi " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Ork zmarł zanim zaatakował")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                else:
                    funkcje.clear()
                    print("Niewłaściwy atak.") 
                    time.sleep(1.3) 
                    funkcje.clear()

            if hpg >= 0 and hporka <= 0:
                print("*******************************************")
                print("Ork poległ.")
                time.sleep(0.3)
                print("Dostajesz 30 PD.")
                print("*******************************************")
                exp = exp + 30
                time.sleep(5)
            elif hporka >= 0 and hpg <= 0:
                print("*******************************************")
                print("Ork wygrał.")
                time.sleep(0.3)
                print("Tracisz 15 PD.")
                print("*******************************************")
                exp = exp - 15
                time.sleep(5)
            else: 
                print("ERROR")
        elif walka == 2:
            print("Omijasz Orka. (- 10 PD)")
            time.sleep(5)
            exp = exp - 10
        return exp


    def lowcawilki():
        
        exp = int()
        print("*******************************************")
        print("Spotykasz na drodze watahę wilków")
        time.sleep(0.3)
        print("Co robisz?")
        print("*******************************************")
        time.sleep(0.3)
        print("1. Podejmuje walkę")
        time.sleep(0.3)
        print("2. Uciekam (- 10 PD)")
        walka = int(input())
        funkcje.clear()
        time.sleep(0.3)
        if walka == 1:
            hpwilka = float(40)
            hpg = float(55) 
            while hpwilka > 0 and hpg > 0 :
                print("*******************************************")
                print("Twoje życie = " + str(hpg))
                time.sleep(0.1)
                print("")
                time.sleep(0.1)
                print("Życie wilków = " + str(hpwilka))
                print("*******************************************")
                time.sleep(0.1)
                print("Wybierz atak:")
                print("*******************************************")
                time.sleep(0.1)
                print("1. Proste zaklęcie (12 - 21 DMG)")
                time.sleep(0.1)
                print("2. Firewall (4 DMG) [blokuje 50% DMG]")
                atak = int(input())
                if atak == 1:
                    multiplierwroga = int(1)
                    t = float(random.randrange(1, 5))
                    if t == 1:
                        zadanydmg = 0
                        print("*******************************************")
                        print("Nie trafiłeś")
                        print("*******************************************")
                        time.sleep(0.6)
                    elif t == 2 or 3 or 4:
                        zadanydmg = float(random.randrange(10, 12))
                        print("*******************************************")
                        print("Trafiłeś")
                        print("*******************************************")
                        time.sleep(0.6)
                    else:
                        zadanydmg = float(random.randrange(15, 18))
                        print("*******************************************")
                        print("Trafiłeś w głowę")
                        print("*******************************************")
                        time.sleep(0.6)
                    dostanydmg = float(random.randrange(7, 10))
                    hpwilka = float(hpwilka - zadanydmg)
                    if hpwilka > 0:
                        hpg = float(hpg - dostanydmg)
                        print("*******************************************")
                        print("Zadałeś wilkom " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Wilki zadały ci " + str(dostanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                    else:
                        print("*******************************************")
                        print("Zadałeś wilkom " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Wilki zmarły zanim zaatakowały")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                elif atak == 2:
                    multiplierwroga = 0
                    zadanydmg = 0
                    dostanydmg = 0
                    hporka = hporka - zadanydmg
                    if hpwilka > 0:
                        hpg = float(hpg - dostanydmg * multiplierwroga)
                        print("*******************************************")
                        print("Zadałeś wilkom " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Wilki zadały ci " + str(dostanydmg * multiplierwroga) + " DMG")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                    else:
                        print("*******************************************")
                        print("Zadałeś wilkom " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Wilki zmarły zanim zaatakowały")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                else:
                    funkcje.clear()
                    print("Niewłaściwy atak.") 
                    time.sleep(1.3) 
                    funkcje.clear()

            if hpg >= 0 and hpwilka <= 0:
                print("*******************************************")
                print("Wilki poległy.")
                time.sleep(0.3)
                print("Dostajesz 25 PD.")
                print("*******************************************")
                exp = exp + 25
                time.sleep(5)
            elif hpwilka >= 0 and hpg <= 0:
                print("*******************************************")
                print("Wilki wygrały.")
                time.sleep(0.3)
                print("Tracisz 13 PD.")
                print("*******************************************")
                exp = exp - 13
                time.sleep(5)
            else: 
                print("ERROR")
        elif walka == 2:
            print("Omijasz wilki. (- 10 PD)")
            time.sleep(5)
            exp = exp - 10
        return exp


    def lowcagolem():
        exp = int()
        print("*******************************************")
        print("Spotykasz na drodze Golema")
        time.sleep(0.3)
        print("Co robisz?")
        print("*******************************************")
        time.sleep(0.3)
        print("1. Podejmuje walkę")
        time.sleep(0.3)
        print("2. Uciekam (- 10 PD)")
        walka = int(input())
        funkcje.clear()
        time.sleep(0.3)
        if walka == 1:
            hpgolem = float(70)
            hpg = float(55) 
            while hpgolem > 0 and hpg > 0 :
                print("*******************************************")
                print("Twoje życie = " + str(hpg))
                time.sleep(0.1)
                print("")
                time.sleep(0.1)
                print("Życie Golema = " + str(hpgolem))
                print("*******************************************")
                time.sleep(0.1)
                print("Wybierz atak:")
                print("*******************************************")
                time.sleep(0.1)
                print("1. Proste zaklęcie (12 - 21 DMG)")
                time.sleep(0.1)
                print("2. Firewall (4 DMG) [blokuje 50% DMG]")
                atak = int(input())
                if atak == 1:
                    multiplierwroga = int(1)
                    t = float(random.randrange(1, 5))
                    if t == 1:
                        zadanydmg = 0
                        print("*******************************************")
                        print("Nie trafiłeś")
                        print("*******************************************")
                        time.sleep(0.6)
                    elif t == 2 or 3 or 4:
                        zadanydmg = float(random.randrange(10, 12))
                        print("*******************************************")
                        print("Trafiłeś")
                        print("*******************************************")
                        time.sleep(0.6)
                    else:
                        zadanydmg = float(random.randrange(15, 18))
                        print("*******************************************")
                        print("Trafiłeś w głowę")
                        print("*******************************************")
                        time.sleep(0.6)
                    dostanydmg = float(random.randrange(6, 9))
                    hpgolem = float(hpgolem - zadanydmg)
                    if hpgolem > 0:
                        hpg = float(hpg - dostanydmg)
                        print("*******************************************")
                        print("Zadałeś Golemowi " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Golem zadał ci " + str(dostanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                    else:
                        print("*******************************************")
                        print("Zadałeś Golemowi " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Golemo zmarł zanim zaatakował")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                elif atak == 2:
                    multiplierwroga = 0
                    zadanydmg = 0
                    dostanydmg = 0
                    hporka = hporka - zadanydmg
                    if hpgolem > 0:
                        hpg = float(hpg - dostanydmg * multiplierwroga)
                        print("*******************************************")
                        print("Zadałeś Golemowi " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Golemo zadał ci " + str(dostanydmg * multiplierwroga) + " DMG")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                    else:
                        print("*******************************************")
                        print("Zadałeś Golemowi " + str(zadanydmg) + " DMG")
                        print("*******************************************")
                        time.sleep(0.2)
                        print("Golemo zmarł zanim zaatakował")
                        print("*******************************************")
                        time.sleep(1.3)
                        funkcje.clear()
                else:
                    funkcje.clear()
                    print("Niewłaściwy atak.") 
                    time.sleep(1.3) 
                    funkcje.clear()

            if hpg >= 0 and hpgolem <= 0:
                print("*******************************************")
                print("Golemo poległ.")
                time.sleep(0.3)
                print("Dostajesz 25 PD.")
                print("*******************************************")
                exp = exp + 25
                time.sleep(5)
            elif hpgolem >= 0 and hpg <= 0:
                print("*******************************************")
                print("Golem wygrały.")
                time.sleep(0.3)
                print("Tracisz 15 PD.")
                print("*******************************************")
                exp = exp - 15
                time.sleep(5)
            else: 
                print("ERROR")
        elif walka == 2:
            print("Omijasz Golema. (- 10 PD)")
            time.sleep(5)
            exp = exp - 10
        return exp


    


