from problem import Problem
import random
from RandomNumberGenerator import RandomNumberGenerator
from utils import defineRandomSwapNeighbour, isDominating, acceptRandomly
import numpy as np

def task3(n, maxIter, seed, numCriteria=4):
    random.seed(seed)

    P = list(list())
    it = 0

    problem = Problem(n, seed)
    x = list(range(n))
    random.shuffle(x)                                           # losowe rozwiązanie początkowe
    P += [(x.copy(), problem.calculateCriteria(x, num_of_criteria=numCriteria))]

    while(it < maxIter): 
        x_prime = defineRandomSwapNeighbour(x)                  # wyznacz x' jako losowego sąsiada x
        if isDominating(                                        # jeśli x' dominuje nad x
            problem.calculateCriteria(x_prime, num_of_criteria=numCriteria), 
            problem.calculateCriteria(x, num_of_criteria=numCriteria)
            ):  
            x = x_prime                                         # wykonaj x <- x'
            P += [(x.copy(), problem.calculateCriteria(x, num_of_criteria=numCriteria))]     # dodaj x' do P
        elif acceptRandomly(p=0.1):                             # w przeciwnym razie wykonaj powyższy etap z prawadopodobieństwem p(it) = 0.1
            x = x_prime                                         # wykonaj x <- x'
            P += [(x.copy(), problem.calculateCriteria(x, num_of_criteria=numCriteria))]     # dodaj x' do P
        it += 1                                                 # it <- it + 1
    
    F = []
    for i in range(len(P)):
        F.append(P[i])
        for j in range(len(P)):
            if isDominating(F[len(F)-1][1], P[j][1])==False and i!=j:
                F.pop()
                break
    print(F)
    while len(F)<4:
        random.shuffle(x)                                           # losowe rozwiązanie początkowe
        F += [(x.copy(), problem.calculateCriteria(x, num_of_criteria=numCriteria))]

    return F