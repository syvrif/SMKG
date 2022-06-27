#!/usr/bin/env python

import random

def main():
    """Jom mulakan permainan teka-teki unsur kimia."""
    print("Teka unsur kimia anda!")
    print("Pilihan jawapan: magnesium, hydrogen, carbon, copper, calcium")

    unsur= [
        "magnesium",
        "hydrogen",
        "carbon",
        "copper",
        "calcium",
        ]

    x = random.choice(unsur)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("Apa unsur kimia yang anda fikirkan?"))
        
        if x == guess:
            print("Anda telah meneka {}. Bagus! Anda meneka dengan betul!".format(guess))
            break
        else:
            print("Anda telah meneka {}. Kurang tepat! Sila cuba lagi!".format(guess))

main()