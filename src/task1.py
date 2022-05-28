from problem import Problem
import random
from RandomNumberGenerator import RandomNumberGenerator
from utils import defineRandomSwapNeighbour, isDominating, acceptRandomly
from matplotlib import pyplot as plt

from data import Data

def task1(n, maxIter):

    P = list(list())
    it = 0

    problem = Problem(n, Data.seed)
    
    x = list(range(n))
    random.shuffle(x)                                           # losowe rozwiązanie początkowe
    P += [(x.copy(), problem.calculateCriteria(x))]             # dodaj x do P

    while(it < maxIter): 
        x_prime = defineRandomSwapNeighbour(x)                  # wyznacz x' jako losowego sąsiada x
        if isDominating(                                        # jeśli x' dominuje nad x
            problem.calculateCriteria(x_prime), 
            problem.calculateCriteria(x)
            ):  
            x = x_prime                                         # wykonaj x <- x'
            P += [(x.copy(), problem.calculateCriteria(x))]     # dodaj x' do P
        elif acceptRandomly(p=0.1):                             # w przeciwnym razie wykonaj powyższy etap z prawadopodobieństwem p(it) = 0.1
            x = x_prime                                         # wykonaj x <- x'
            P += [(x.copy(), problem.calculateCriteria(x))]     # dodaj x' do P
        it += 1                                                 # it <- it + 1
    
    P = sorted(P, key=lambda x: int(x[1][0]))
    
    print(P)
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    xDim=[]
    yDim=[]
    xFront=[]
    yFront=[]
    frontVal=P[0][1][1]
    for solution in P:
        xDim.append(solution[1][0])
        yDim.append(solution[1][1])
        if solution[1][1]<=frontVal:
            xFront.append(solution[1][0])
            yFront.append(solution[1][1])
            frontVal=solution[1][1]
    plt.xlim(0, 10000)
    plt.ylim(0, 10000)
    plt.grid()
    plt.scatter(xDim, yDim, marker="o", edgecolors="blue")#, markerfacecolor="green")
    plt.scatter(xFront, yFront, marker="o", edgecolors="red")#, markerfacecolor="green")
    plt.show()