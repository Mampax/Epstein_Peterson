#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Program służący do wyznaczenia strat dyfrakcyjnych metodą Epsteina-Petersona

import math


# Obliczanie efektywnej wysokości
def effective_height(h, dist, count):
    count = count - 2
    for x in range(count):
        k = float(h[x + 1] - h[x] - ((dist[x] * (h[x + 2] - h[x])) / (dist[x] + dist[x + 1])))
        eh.append(k)
    return eh


# Obliczanie parametru dyfrakcji
def diffraction_parametr(count, eh, dist, frequency):
    count = count - 2
    for x in range(count):
        k = float(eh[x] * (math.sqrt((2 * (dist[x] + dist[x + 1])) / ((300 / frequency) * dist[x] * dist[x + 1]))))
        v.append(k)
    return v

def view(h, dist, eh, v):
    print("Wysokości kolejnych przeszkód wynoszą: {} m".format(h))
    print("Odległości między kolejnymi przeszkodami wynoszą: {} m".format(dist))
    print("Efektywne wysokości dla kolejnych przeszkód wynoszą: {} m".format(eh))
    print("Parametry dyfrakcji dla kolejnych przeszkód wynoszą: {}\n\n\n".format(v))
    return None

finish = 0 #Obsługa menu
while finish != 3:

    print("Wyznaczanie strat dyfrakcyjnych metodą Epsteina-Petersona \n\n MENU\n1) Wczytaj dane z pliku\n2) Podaj ręcznie\n3) Wyjdź")
    dist = []  # tablica odległości między przeszkodami
    h = []  # wysokości obiektów
    eh = []  # tablica efektywnych wysokości
    v = [] # tablica parametrów dyfrakcji
    choice = int(input("Wybór: "))  # opcja z menu

    if choice == 1 or choice == 2:
        frequency = float(input("Częstotliwość [MHz]: "))  # Podanie częstotliwości

    if choice == 1:
        # Wczytanie wysokości obiektów z pliku
        print("In progress")
        file_h = open("heights.txt", "r")
        for x in file_h:
           h.append(float(x))
        file_h.close()
        count = len(h)
        # Wczytanie odległości między obiektami z pliku
        file_d = open("distances.txt", "r")
        for x in file_d:
            dist.append(float(x))
        file_d.close()
        # Obliczanie efektywnej wysokości
        eh = effective_height(h, dist, count)
        # Obliczanie parametrów dyfrakcji
        v = diffraction_parametr(count, eh, dist, frequency)
        # Wyświetlenie danych
        view(h, dist, eh, v)

    # Ręczne wprowadzanie danych
    elif choice == 2:
        if frequency <= 0: # Częstotliwość nie może być mniejsza od 0 [MHz]
            print("Zła wartość")
            break;
        count = int(input("Ilość przeszkód na trasie propagacji: ")) #liczba przeszkód między nadajnikiem a odbiornikiem

        if count < 1: #liczba przeszkód na trasie nie może być mniejsza od 1
            print("Zła wartość. Liczba przeszkód na trasie nie może być mniejsza od 1")
            break;

        count = count + 2 #powiększenie ilości przeszkód o nadajnik i odbiornik

        # Wprowadzenie wysokości obiektów
        print("Wysokości nadajnika, odbiornika i przeszkód:")
        for x in range(count):
            if x == 0:
                k = int(input("     - Wysokość nadajnika [m]:  "))
                h.append(k)
            elif x == count - 1 and x != 0:
                k = int(input("     - Wysokość odbiornika [m]:  "))
                h.append(k)
            else:
                k = int(input("     - Wysokość przeszkody nr {} [m]: ".format(x)))
                h.append(k)

        # Wprowadzenie odległości między obiektami
        print("Odległośći między kolejnymi przeszkodami")
        for x in range(count - 1):
            if x == 0:
                k = int(input("     - Odległość między nadajnikiem a przeszkodą nr 1 [m]:  "))
                dist.append(k)
            elif x == count - 2 and x != 0:
                k = int(input("     - Odległość między ostatnią przeszkodą a odbiornikiem [m]:  "))
                dist.append(k)
            else:
                k = int(input("     - Odległość między przeszkodzą nr {}, a przeszkodą nr {} [m]: ".format(x, x + 1)))
                dist.append(k)

        # Obliczanie efektywnej wysokości
        eh = effective_height(h, dist, count)
        # Obliczanie parametrów dyfrakcji
        v = diffraction_parametr(count, eh, dist, frequency)
        # Wyświetlenie danych
        view(h, dist, eh, v)

    elif choice == 3:
        finish = 3

    else:
        print("Zła liczba. Brak takiej wartości do wyboru!")


