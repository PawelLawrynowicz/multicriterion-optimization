import random
from problem import Problem
from data import Data
from utils import defineRandomSwapNeighbour, acceptRandomly

random.seed(Data.seed)

def s(x):
    c = [1,5,5]
    sum = 0
    for i in range(len(x)):
        sum += x[i]*c[i]
    return sum

def task2(n, maxIter, output = False):
    it = 0                                                  # it <- 0

    problem = Problem(n, Data.seed)

    x = list(range(n))                                      # losowe rozwiązanie początkowe
    random.shuffle(x)                                       

    x = problem.calculateCriteria(x, num_of_criteria=3)


    x_best = s(x)                                           # wykonaj x_best <- s(x)

    while (it < maxIter):                                   # dopóki it < maxIter
        x_prime = defineRandomSwapNeighbour(x)              # wyznacz x' jako losowego sąsiada x
        if s(x_prime) < s(x):                               # jeśli s(x') < s(x)
            x = x_prime                                         # wykonaj x <- x'
            x_best = x_prime                                    # wykonaj x_best <- x'
        elif acceptRandomly(p=0.1):                         # w przeciwnym razie
            x = x_prime                                         # wykonaj x <- x' z pradopodobieństwem p(it)
        it += 1                                             # it <- it + 1

    if s(x_best) < s(x):
        x = x_best 
    
    if output:
        print(f"x:\t{x}\ns(x):\t{s(x)}")                        # wypisz x