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

    fig, ax = plt.subplots(4,2)
    fig.tight_layout() 
    columnNum=0
    plotNum=0
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
        if it%200==0:
            xDim=[]
            yDim=[]
            xFront=[]
            yFront=[]
            frontVal=P[0][1][1]
            for solution in P:
                if solution[1][1]<=frontVal:
                    xFront.append(solution[1][0])
                    yFront.append(solution[1][1])
                    frontVal=solution[1][1]
                    continue
                xDim.append(solution[1][0])
                yDim.append(solution[1][1])
            #plt.xlim(0, 10000)
            #plt.ylim(0, 10000)
            ax[plotNum][columnNum].set_title("{iters} iters".format(iters=it))
            ax[plotNum][columnNum].grid()
            ax[plotNum][columnNum].scatter(xDim, yDim, marker="o")#, markerfacecolor="green")
            ax[plotNum][columnNum].plot(xFront, yFront, '-o', mec="red", mfc="red", color="red")#, markerfacecolor="green")
            plotNum+=1
            if plotNum == 4: 
                plotNum=0
                columnNum+=1
    plt.show()

    #plt.figure("HVI")
