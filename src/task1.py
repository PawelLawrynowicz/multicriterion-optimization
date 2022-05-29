from problem import Problem
import random
from RandomNumberGenerator import RandomNumberGenerator
from utils import defineRandomSwapNeighbour, isDominating, acceptRandomly
from matplotlib import pyplot as plt
import itertools
from data import Data

def task1(n, maxIter):

    marker = itertools.cycle(('o', 's', 'D', '*')) 
    colors = itertools.cycle(('b', 'r', 'g', 'm'))

    P = list(list())
    it = 0

    problem = Problem(n, Data.seed)
    
    x = list(range(n))
    random.shuffle(x)                                           # losowe rozwiązanie początkowe
    P += [(x.copy(), problem.calculateCriteria(x))]             # dodaj x do P

    fig1, ax1 = plt.subplots(4,2)
    fig1.tight_layout() 
    fig2, ax2 = plt.subplots(1)
    fig2.tight_layout() 
    columnNum=0
    plotNum=0


    zX = 0
    zY = 0
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
    
        
        
        
        if it%200==0:
            P = sorted(P, key=lambda x: int(x[1][0]))
            if it==200:
                zX = P[len(P)-1][1][0]*1.2
                zY = P[len(P)-1][1][1]*1.2
                ax2.grid()
                ax2.scatter(zX, zY, color='k',marker='>')
                ax2.annotate("Z",(zX, zY))
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

            ax1[plotNum][columnNum].set_title("{iters} iters".format(iters=it))
            ax1[plotNum][columnNum].grid()
            ax1[plotNum][columnNum].scatter(xDim, yDim, marker="o")#, markerfacecolor="green")
            ax1[plotNum][columnNum].plot(xFront, yFront, '-o', mec="red", mfc="red", color="red")#, markerfacecolor="green")
            
            #fig2.set_title("{iters} iters".format(iters=it))
            if it%400==0:
                ax2.grid()
                colour = next(colors)
                ax2.scatter(xFront, yFront, marker=next(marker),color=colour)
                xFront.append(zX)
                xFront.append(zX)
                xFront.append(xFront[0])
                yFront.append(yFront[len(yFront)-1])
                yFront.append(zY)
                yFront.append(zY)
                ax2.fill(xFront, yFront, color=colour,alpha=.2)

                #calc and plot hvi

                
            
            #ax[plotNum][columnNum].fill(xFront, yFront, 'y', alpha=0.5)
            plotNum+=1
            if plotNum == 4: 
                plotNum=0
                columnNum+=1
            
            
    plt.show()

    #plt.figure("HVI")
