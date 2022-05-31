from problem import Problem
import random
from RandomNumberGenerator import RandomNumberGenerator
from utils import defineRandomSwapNeighbour, isDominating, acceptRandomly
import numpy as np
import matplotlib.pyplot as plt

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

    data_span = []
    for i in range(numCriteria):
        data_span.append([F[0][1][i],F[0][1][i]])
    for sol in F:
        for i, val in enumerate(sol[1]):
            if(val<data_span[i][0]):
                data_span[i][0]=val
            if(val>data_span[i][1]):
                data_span[i][1]=val

    while len(F)>3:
        F.pop(random.randint(0, len(F)-1))
    while len(F)<4:
        random.shuffle(x)                                           # losowe rozwiązanie początkowe
        F += [(x.copy(), problem.calculateCriteria(x, num_of_criteria=numCriteria))]
        print("rozwiazanie losowe: {sol}".format(sol=F[len(F)-1]))

    for sol in F:
        for i, val in enumerate(sol[1]):
            if(val<data_span[i][0]):
                data_span[i][0]=val
            if(val>data_span[i][1]):
                data_span[i][1]=val

    criteria = []
    solutions = []
    labels = []
    for i, sol in enumerate(F):
        solutions.append(sol[1])
        labels.append("rozwiązanie {num}".format(num=i+1))
        print(sol[1])
    for i in range(numCriteria):
        criteria.append("kryterium {num}".format(num=i+1))

    for i, solution in enumerate(solutions):
        plt.plot(criteria, solution, label = labels[i])
        plt.legend()
        plt.title("Ścieżki wartości")
        plt.ylabel("wartość kryterium")

    for i in range(len(criteria)):
        plt.scatter(criteria[i], data_span[i][0], c='black')
        plt.scatter(criteria[i], data_span[i][1], c='black')
    
    print("data span: {span}".format(span=data_span))
    
    plt.grid()
    plt.show()

