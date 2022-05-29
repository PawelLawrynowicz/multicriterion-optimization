# 1356 2456
"""
Zadanie 1: KO: 1, 3
Zadanie 2: KO: 1, 3, 5
Zadanie 3: Wszystko

Kryteria optymalizacji:
1. Czas zakończenia wszystkich zadań (makespan).
3. Maksymalne spóźnienie zadania (max tardiness).
5. Maksymalna nieterminowość zadania (max lateness).
6. Suma nieterminowości zadań (total lateness).

Metody wizualizacji:
2. Ścieżki wartości (value paths)
4. Współrzędne gwiazdowe (star coordinates)
5. Odcinkowe współrzędne gwiazdowe (star coordinate system with line segments)
6. Wykresy pajęczynowe (spider web charts).
"""

from task1 import task1
from data import Data


if __name__ == '__main__':

    # zadanie 3
    task1(Data.n, Data.maxIter, numCriteria=4)