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
from task2 import task2
from task3 import task3
from data import Data

def save_task2_data():
    # zadanie 2
    seeds = [1410, 9674, 155, 3486, 7158, 5325, 9742, 7081, 992, 3122]
    f = open("pomiary_zad2.csv", "w")
    for it, seed in enumerate(seeds):
        Data.seed = seed
        f.write("Przebieg " + str(it+1) + " seed: " + str(seed) + "\n")
        result = task2(Data.n, Data.maxIter, output=False)
        for i, val in result.items():
            f.write(str(i)+";"+str(val)+"\n")

if __name__ == '__main__':
    print(task3(Data.n,Data.maxIter,Data.seed))
