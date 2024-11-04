#!/bin/python

# ******************************************************
#  nazwa klasy: Film
#  pola: __title - (str) Tytuł filmu
#        __rentals - (int) Liczba wypożyczeń filmu
#  metody: getTitle, (str) Tytuł filmu – Zwraca tytuł filmu
#          setTitle, (None) nic – Ustawia tytuł filmu
#          getRentals, (int) Liczba wypożyczeń filmu – Zwraca liczbę wypożyczeń filmu
#          increment, (None) nic – Zwiększa o 1 liczbę wypożyczeń filmu
#  informacje: Klasa przechowuje dane dotyczące filmu oraz pozwala na operację związane z wypożyczaniem
#  autor: XYZ
# *****************************************************
class Film:
    __title: str = None
    __rentals: int = 0

    def getTitle(self) -> str:
        return self.__title

    def setTitle(self, title: str) -> None:
        self.__title = title
        
    def getRentals(self) -> int:
        return self.__rentals

    def increment(self) -> None:
        self.__rentals += 1

# Start
print("Program testujący system wirtualnej wypożyczalni filmów")
film = Film()
print(f"Pola obiektu po inicjalizacji:\nTytuł: {film.getTitle()}\nWypożyczenia: {film.getRentals()}")
film.setTitle("Blade Runner 2049")
film.increment()
print(f"Pola obiektu po ustawieniu danych:\nTytuł: {film.getTitle()}\nWypożyczenia: {film.getRentals()}")
