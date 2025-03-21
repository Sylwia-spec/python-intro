# Laboratoria 1

'''
Importowanie modułu random
W języku Python przewidziano moduł random generujący liczby pseudolosowe.
Dokumentacja: https://docs.python.org/3/library/random.html
'''

import random

# Tworzenie dwóch list
lista1 = [5, 12, 50, 111]
lista2 = ['s', 'y', 'l', 'a']

'''
Łączenie list za pomocą funkcji zip() - Funkcja zip łączy ze sobą elementy z różnych obiektów iterowalnych, takich jak listy, krotki, zbiory, i zwraca nam iterator. 
Możemy jej użyć to połączenia ze sobą dwóch list.
Dokumentacja: https://docs.python.org/3/library/functions.html#zip
'''
zipped = list(zip(lista1, lista2))
print("Połączone listy:", zipped)

'''
Wylosowanie liczby z listy - w celu uzyskania losowej liczby niezbędne jest skorzystanie z funkcji "random".
Po zaimportowaniu modułu możemy korzystać z wielu funkcji, m.in. losujacych wartość z podanego zakresu, zmieniających w losowy sposób kolejność elementów na liście, wybierających losową wartość spośród podanych.
W naszym przypadku funkcja random wylosowała liczbę ze wskazanej listy.
Dokumentacja: https://docs.python.org/3/library/random.html#random.choice
'''
losowa_liczba = random.choice(lista1)
print("Losowa liczba:", losowa_liczba)

'''
Obsługa wyjątku - Błędy zauważone podczas wykonania programu są nazywane wyjątkami (exceptions).
Większość wyjątków nie jest obsługiwana przez program przez co wyświetlane są informacje o błędzie.
Możliwe jest pisanie programów, które obsługują wybrane wyjątki.
ZeroDivisionError to wyjątek w Pythonie, który występuje, gdy próbujemy podzielić liczbę przez zero.
Aby uniknąć zatrzymania programu, możemy użyć bloku try-except, który przechwyci błąd i pozwoli programowi kontynuować działanie.
Dokumentacja: https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
'''
# Celowe wywołanie ZeroDivisionError
try:
    wynik = losowa_liczba / 0
except ZeroDivisionError:
    print("Błąd: Nie wolno dzielić przez zero!")